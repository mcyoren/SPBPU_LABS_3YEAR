#include "Format.h"
#include "TEllipse.h"
void rombs_draw_sep (int lb, int rb)
{



    double Nev_exp[7]={200,150,100,75,50,25,15};
    double msize[7]={4.,3.2,3.4,1.,1.2,1.8,2.1};
    double bigs[7]={20,20,15,8,8,12,15};
    double big_scale[7]={1,1,1.25,2.5,2.2,1.5,1.5};
 //1****************start initialization************************************
    TCanvas *c1;

    TEllipse *el1 = new TEllipse(0.5,0.5,0.5,0.5);
    el1->SetFillColor(kGreen+2);
    el1->SetLineWidth(0);
    el1->SetFillStyle(3023);

    TF1 *radi, *size, *phi, *transpar;
    radi = new TF1("radi","[0]+x",0.,0.49);
    phi = new TF1("phi","x",0,3.14159*20);
    transpar = new TF1("transpar","x",0.2,0.8);
    TMarker *romb, *romb_inner, *romb_big, *romb_big_inner;

    for (int icircule = lb; icircule < rb; ++icircule) {

        c1 = new TCanvas("c1","c1",9000,9000);
        Format_Canvas(c1,1,1,0);
        c1->SetFillColor(kGreen+1);
        TPad *c1_1= (TPad*) c1->GetListOfPrimitives()->FindObject("c1_1");
        c1_1->SetFillColor(kGreen+1);

        size = new TF1("size","x",0.5*msize[icircule],msize[icircule]);
        el1->Draw();

        for (int i = 0; i < Nev_exp[icircule]*60; ++i) {
            double iradi = radi->GetRandom();
            double iphi = phi->GetRandom();
            double isize=size->GetRandom();
            romb= new TMarker(0.5+iradi*cos(iphi),0.5+iradi*sin(iphi),33);
            romb->SetMarkerSize(isize);
            romb->SetMarkerColorAlpha(1,1);
            romb->Draw();
            romb_inner= new TMarker(0.5+iradi*cos(iphi),0.5+iradi*sin(iphi),33);
            romb_inner->SetMarkerSize(isize*(0.5+0.5*transpar->GetRandom()));
            romb_inner->SetMarkerColorAlpha(kGreen+2,transpar->GetRandom());
            romb_inner->Draw();
        }
        for (int i = 0; i < Nev_exp[icircule]*60/bigs[icircule]; ++i) {
            double iradi = radi->GetRandom();
            double iphi = phi->GetRandom();
            double isize=size->GetRandom()*big_scale[icircule]+big_scale[icircule]*msize[icircule];
            romb_big= new TMarker(0.5+iradi*cos(iphi),0.5+iradi*sin(iphi),33);
            romb_big->SetMarkerSize(isize);
            romb_big->SetMarkerColorAlpha(1,1);
            romb_big->Draw();
            romb_big_inner= new TMarker(0.5+iradi*cos(iphi),0.5+iradi*sin(iphi),33);
            romb_big_inner->SetMarkerSize(isize*(0.2+transpar->GetRandom()));
            romb_big_inner->SetMarkerColorAlpha(kGreen+2,transpar->GetRandom());
            romb_big_inner->Draw();
        }

        char name[200];
        sprintf(name,"output/rombs_%d.png",icircule);
        c1->SaveAs(name);
    }

}


