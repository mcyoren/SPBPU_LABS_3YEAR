import random, math, pygame, os, time
from tkinter import *
from scipy import integrate

# ==============init================
e = math.exp(1)
c = 2.998e8
pi = math.pi
Proc_of_mu = 0.7
mu_hard = 0.001
mu_soft = 0.3
mu_air = 5.6e-7
tau_mu_pos = 2.2e-6
tau_mu_neg_air = 2.2e-6
tau_mu_neg_Pb = 7.e-8
eps_eff = 0.5
R_earh = 6371000
L = 15000
theta_range = 0.00135#pi/2
phi_range = pi
x_lenght = 4
y_lenght = 6
z_lenght = 20
dzed = 6
dlen_max = [0, 1, 2, z_lenght/dzed+3, z_lenght/dzed + 4]
dlen_min = [0, 1, z_lenght/dzed+2, z_lenght/dzed + 3]
tot_sq = 4*dzed*y_lenght+y_lenght*z_lenght+47
E = 4000
m = 105.4
global Detector
Detector = [0, 0, 0, 0, 0, 0]
global ss, n_time, Nhelp
ss = 0
n_time = 0
Nhelp = 0

#===========================
N_iter = 100
angel_s = lambda x: 2*pi*R_earh**2*math.tan(x)/math.cos(x)/math.sqrt(R_earh**2+(R_earh+L)**2-2*R_earh*(R_earh+L)*math.cos(x))
tot_angel_s = [int(integrate.quad(angel_s, 0, theta_range*i/N_iter)[0]) for i in range(N_iter + 1)]
print(tot_angel_s)
# ===========Def==============
def cot(alpha):
    return math.tan(pi/2-alpha)
def dist(a, b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)
def plane_angle(a, b):
    xxx = abs(a[0]*b[0]+a[1]*b[1]+a[2]*b[2])
    xxx /= math.sqrt(a[0]**2+a[1]**2+a[2]**2)*math.sqrt(b[0]**2+b[1]**2+b[2]**2)
    cucl_angle = math.asin(xxx)
    return cucl_angle
def line_angle(a, b):
    xxx = abs(a[0]*b[0]+a[1]*b[1]+a[2]*b[2])
    xxx /= math.sqrt(a[0]**2+a[1]**2+a[2]**2)*math.sqrt(b[0]**2+b[1]**2+b[2]**2)
    if xxx > 1 or xxx < 0:
        xxx = 1.
    cucl_angle = math.acos(xxx)
    return cucl_angle
def vec_angle(a, b):
    xxx = a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    xxx /= math.sqrt(a[0]**2+a[1]**2+a[2]**2)*math.sqrt(b[0]**2+b[1]**2+b[2]**2)
    cucl_angle = math.acos(xxx)
    return cucl_angle
def line_proj(a, b):
    xxx = a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    xxx /= b[0]**2+b[1]**2+b[2]**2
    proj = [a[i] - xxx*b[i] for i in range(3)]
    return proj
def Start(width_scale, angle_scale, time_scale, speed_scale, meth_scale, startstop):
    global ss, Detector, n_time
    ss += startstop
    nproc = 500
    tproc = 3.67e-2
    if meth_scale < 4:
        nproc *= 2
    t_delay = max(1, int(1000/speed_scale - tproc*nproc))
    Process(nproc, width_scale, angle_scale)
    Window1_text['text'] = ' '.join(str(Detector[meth_scale]))
    if ss % 2 == 1:
        if n_time < time_scale*60 - 1:
            Window1_text.after(t_delay, lambda: Start(width_scale, angle_scale, time_scale, speed_scale, meth_scale, 0))
            n_time += 1
        else:
            print('end')
    else:
        Detector = [0, 0, 0, 0, 0, 0]
        Window1_text['text'] = ' '.join(str(Detector[meth_scale]))
        n_time = 0
    # =========Begin code==============
def Process(N_ev, width_Pb, angle_det):
    for _ in range(0, N_ev):
        # =========Init of part==============

        isDetected = [0, 0]
        isAim = [0, 0, 0, 0]
        theta_ray_s = int(random.random()*tot_angel_s[N_iter-1])
        theta_ray = - 9999
        for i in range(N_iter):
            if tot_angel_s[i] < theta_ray_s <= tot_angel_s[i+1]:
                theta_ray = theta_range*i/N_iter+theta_range/N_iter*random.random()
        #theta_ray = math.sqrt(random.random() * theta_range)
        phi_ray = random.random() * phi_range
        R_Zemly = [0, 0, R_earh/(R_earh+L)]
        R_Cosmos = [math.sin(theta_ray)*math.cos(phi_ray), math.sin(theta_ray)*math.sin(phi_ray), math.cos(theta_ray)]
        raduis_vex = [R_Cosmos[i]-R_Zemly[i] for i in range(3)]
        distance = dist(R_Zemly, R_Cosmos)*(R_earh+L)
        theta = line_angle(raduis_vex, R_Cosmos)
        phi_vec = line_proj(raduis_vex, [0,0,1])
        phi = vec_angle(phi_vec, [1,0,0])
        theta_det = angle_det*pi/180
        xy_vec = [math.tan(theta_det), 0, 1]
        xz_vec = [-1, 0, math.tan(theta_det)]
        yz_vec = [0, 1, 0]
        angel = [plane_angle(raduis_vex, xy_vec), plane_angle(raduis_vex, xz_vec), plane_angle(raduis_vex, yz_vec)]
        sq_xy = x_lenght *y_lenght*math.sin(angel[0])
        sq_xz = dzed * y_lenght * math.sin(angel[1])
        sq_yz = dzed * x_lenght * math.sin(angel[2])
        pr_xy = line_proj(raduis_vex, xy_vec)
        phi_rp = line_angle(xz_vec, pr_xy)
        #print(theta * 180 / pi, phi * 180 / pi, angel[0] * 180 / pi, phi_rp * 180 / pi, angel[1] * 180 / pi, angel[2] * 180 / pi)
        det_sq_max = [sq_xy + dlen_max[i]*(sq_xz + sq_yz) for i in range(0, 5)]
        det_sq_min = [dlen_min[i]*(sq_xz + sq_yz) for i in range(0, 4)]
        if det_sq_max[4] > tot_sq:
            print(det_sq_max[4])
        square = random.random()*tot_sq
        print(square, det_sq_max)
        if square > det_sq_max[4] or square > det_sq_max[2] and square < det_sq_min[2]:
            continue
        for i in range(0, 4):
            if det_sq_min[i] < square < det_sq_max[i+1]:
                isAim[i] = 1
       # beta = math.asin(R_earh/(R_earh+L)*math.sin(theta))
        #theta_ray = theta - beta
        #distance = math.sqrt(R_earh**2 + (R_earh+L)**2-2*R_earh*(R_earh+L)*math.cos(theta_ray))
        """if meth > 3 and (abs(dtheta) > math.atan(xx/z_lenght) or abs(phi) > math.atan(yy/z_lenght)):
            continue"""
        prob_dec = 1
        rand = random.random()
        rand1 = random.random()
        mu = mu_soft
        if rand <= Proc_of_mu:
            mu = mu_hard
            if rand1 < 0.5:
                tau = tau_mu_pos
            else:
                tau = tau_mu_neg_air
                prob_dec *= e ** (-width_Pb/c / tau_mu_neg_Pb)
            # ======decay before det============
            rand_dec = random.random()
            t_mu = distance/c*m/E
            prob_dec *= e ** (-t_mu / tau)
            #print(prob_dec, distance)
            if prob_dec*(math.cos(theta*1.5)**1.6) < rand_dec:
                continue
        else:
            rand_soft = random.random()
            prob_soft = e**(-mu_air*distance*100)
            if rand_soft > prob_soft*(math.cos(theta*1.5)**1.6):
                continue
        # ===========first two det=================
        for idet in range(0, 2):
            rand_det = random.random()
            if rand_det < eps_eff:
                Detector[idet] += isAim[idet]
                isDetected[0] += isAim[idet]
        # ===========scattering=================
        if isAim[2] == 0 and isAim[3] == 0:
            continue
            
        rand_scat = random.random()
        prob_scat = e ** (-mu * width_Pb)
        if prob_scat < rand_scat:
            continue
        # ===========final detectors=================
        for idet in range(2, 4):
            rand_det = random.random()
            if rand_det < eps_eff:
                Detector[idet] += isAim[idet]
                isDetected[1] += isAim[idet]
        # ============Counts========================
        if isDetected[0] >= 1 and isDetected[1] >= 1:
            print(phi * 180 / pi, theta * 180 / pi, angel[0]*180/pi, angel[1]*180/pi, angel[2]*180/pi,)
            Detector[4] += 1
        if isDetected[0] == 2 and isDetected[1] == 2:
            Detector[5] += 1


# =========================Windowed=================================
root = Tk()
root.title("Labs: Cosmos")

width = 500
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
window_size = int(screen_width / 2)
# ================================FRAMES=========================================
Top = Frame(root, width=600, bd=1, relief=SOLID)
Top.pack(side=TOP)
But0 = Frame(root, width=200, height=50, bd=1, relief=SOLID)
But0.place(x=width/2-100, y=height*0.9)
Window1 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
Window1.place(x=width/2-25, y=height*0.5-25)
Scale1 = Frame(root, width=50, height=50, bd=1, bg='white')
Scale1.place(x=width/10, y=height/5)
Scale2 = Frame(root, width=50, height=50, bd=1, bg='white')
Scale2.place(x=width/10*2.5, y=height/5)
Scale3 = Frame(root, width=50, height=50, bd=1, bg='white')
Scale3.place(x=width/10*6.5, y=height/5)
Scale4 = Frame(root, width=50, height=50, bd=1, bg='white')
Scale4.place(x=width/10*8, y=height/5)
Scale5 = Frame(root, width=50, height=50, bd=1, bg='white')
Scale5.place(x=width/10*2, y=height/10)

# ================================LABEL WIDGETS==================================
# ================================LABEL WIDGETS==================================
lbl_title = Label(Top, text="KoronaLab", width=600, font=("arial", 20))
lbl_title.pack(fill=X)
Scale1 = Scale(Scale1, orient=VERTICAL, length=300, from_=9, to=0, tickinterval=1, resolution=1)
Scale1.pack()
Scale2 = Scale(Scale2, orient=VERTICAL, length=300, from_=100, to=1, tickinterval=10, resolution=1)
Scale2.pack()
Scale3 = Scale(Scale3, orient=VERTICAL, length=300, from_=90, to=0, tickinterval=15, resolution=5)
Scale3.pack()
Scale4 = Scale(Scale4, orient=VERTICAL, length=300, from_=120, to=1, tickinterval=10, resolution=1)
Scale4.pack()
Scale5 = Scale(Scale5, orient=HORIZONTAL, length=300, from_=6, to=1, tickinterval=1, resolution=1)
Scale5.set(5)
Scale5.pack()
lbl_text0 = Label(But0, text="Start/STOP", font=("arial", 30))
lbl_text0.bind("<Button-1>", lambda _: Start(Scale1.get(), Scale3.get(), Scale4.get(), Scale2.get(), Scale5.get() - 1, 1))
lbl_text0.pack()

Window1_text = Label(Window1, bg='black', fg='white', font=("arial", 20))
Window1_text.pack()

# ================================INITIALIZATION=================================

if __name__ == '__main__':
    root.mainloop()
