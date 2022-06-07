#include "Format.h"
#include "TLine.h"
#include "TEllipse.h"

double path(double Rtot, double mass, int charge);
void draw_star(double x, double y, double transparency);
void draw_twodec(double x, double y, double transparency, double dec);

void carrots () {


    double multipl=(7.+3+7+4+3+7+7+3+4+4+5+5+2+5+3+4+3+7+3+6+4+6+3+3+6+3+4+4+3+4+4+2+0+7+5+5+7+3+5+4+3+5+5+4+4+4+5+3+5+3+7+3)/50;//4.5

    double path_range[8];

    path_range[0]=path(431,40,18);//Ar40 505
    path_range[1]=path(431,56,26);//Fe56 505
    path_range[2]=path(544,56,26);//Fe56 583
    path_range[3]=path(1185,56,26);//Fe56 1000
    path_range[4]=path(1420,197,79);//Au197 1142
    path_range[5]=path(1064,238,92);//U238 927
    path_range[6]=path(1064,238,92);//U238 927
    path_range[7]=path(1064,238,92);//U238 927

    for (int k = 0; k < 6; ++k) {
        cout<<path_range[k]<<endl;
    }

    TCanvas *c1;
    c1 = new TCanvas("c1", "c1", 9000, 9000);
    Format_Canvas(c1, 1, 1, 0);
    c1->SetFillColor(kGreen + 1);
    c1->SetFillStyle(3001);
    TPad *c1_1 = (TPad *) c1->GetListOfPrimitives()->FindObject("c1_1");
    c1_1->SetFillColor(kGreen + 1);
    c1_1->SetFillStyle(3001);
    c1_1->SetTopMargin(0.05);



    TLine *line;
    line = new TLine(0,0,0,1);
    line->SetLineWidth(2);
    TLatex *tex;
    char name[200];
    for (int i = 0; i < 102; ++i) {
        line->DrawLine(0,0.01*i,1,0.01*i);
        line->DrawLine(0.01*i,0,0.01*i,1);
        for (int j = 0; j < 102; ++j) {
            sprintf(name,"%d",00+i);
            tex= new TLatex(0.01*i+0.0036,0.01*j+0.0025,name);
            tex->SetTextSize(0.003);
            tex->Draw();
            sprintf(name,"%d",abs(50-j));
            tex= new TLatex(0.01*i+0.0036,0.01*j+0.0055,name);
            tex->SetTextSize(0.003);
            tex->Draw();
        }
    }


    TF1 *transpar, *yy, *dely, *par_type, *path_per, *decay;
    par_type = new TF1("par_type","x",0,8);
    yy = new TF1("yy","x",0,1);
    dely = new TF1("dely","x",-3.14159*2/180,3.14159*2/180);
    transpar = new TF1("transpar","x",0.05,0.25);
    path_per = new TF1("transpar","x",0.95,1.05);
    decay = new TF1("decay","x",0.,1.);

    TLine *carrot;
    carrot = new TLine(0,0,0,1);
    carrot->SetLineWidth(1);

    for (int i = 0; i < 455; ++i) {
        double iyy=yy->GetRandom();
        int type =(int) par_type->GetRandom();
        double ixx=1.-path_range[type]*path_per->GetRandom()/100;
        double del=ixx*sin(dely->GetRandom())/100;
        double itranspar=transpar->GetRandom();
        double idecay=decay->GetRandom();
        carrot->SetLineColorAlpha(1,itranspar);
        carrot->DrawLine(ixx,iyy+del,1,iyy);
        carrot->DrawLine((ixx*9+1)/10,iyy+del*9/10,1,iyy);
        carrot->DrawLine((ixx*7+3)/10,iyy+del*7/10,1,iyy);
        carrot->DrawLine((ixx*4+6)/10,iyy+del*4/10,1,iyy);
        if(type==4&&idecay>0.9)draw_star(ixx,iyy+del,itranspar*0.5);
        if(type>4&&idecay>0.7)draw_twodec(ixx,iyy+del,itranspar*0.5,idecay);
    }

    c1->SaveAs("output/carrots.png");
    c1->SaveAs("output/carrots.jpeg");
}


double path(double Rtot, double mass, int charge){
    double ipath=mass*0.931/charge/charge*Rtot-1.8/10000*mass*0.931*pow(charge,2./3);
    return ipath;
}

void draw_star(double x, double y, double transparency)
{
    TLine *linestar = new TLine(0,0,0.1,0.1);
    linestar->SetLineColorAlpha(1,transparency);
    for (int i = 0; i < 5; ++i) {
        linestar->DrawLine(x,y,x+0.0005*cos(-i*3.14159/2.5+3.14159/5),y+0.0005*sin(-i*3.14159/2.5+3.14159/5));
    }
}
void draw_twodec(double x, double y, double transparency, double dec)
{
    double klengh=2.5;
    double xxx[2][5], yyy[2][5];
    for (int j = 0; j < 5; ++j) {
        xxx[0][j]=x-0.002*j*(dec-0.2)*(dec-0.2)*4*klengh;
        yyy[0][j]=y+0.0003*j*j*(dec-0.5)*(0.85-dec)/fabs(0.85-dec)*klengh;
        xxx[1][j]=x-0.001*j*(dec-0.2)*(dec-0.2)*4*klengh;
        yyy[1][j]=y-0.001*j*j*(dec-0.5)*(0.85-dec)/fabs(0.85-dec)*klengh;
    }
        TGraph *graph[2];
    for (int i = 0; i < 2; ++i) {
        graph[i]=new TGraph(5,xxx[i],yyy[i]);
        graph[i]->SetLineColorAlpha(1,transparency);
        graph[i]->Draw("same");
    }

}