#include "Format.h"
#include "TEllipse.h"
#include "math.h"
void rombs_draw (int pr)
{

    double Nev_exp[7]={200,150,100,75,50,25,15};
 //1****************start initialization************************************
    TCanvas *c1 = new TCanvas("c1","c1",9000,1500);
    Format_Canvas(c1,1,1,0);
    c1->SetFillColor(kGreen+1);
    TPad *c1_1= (TPad*) c1->GetListOfPrimitives()->FindObject("c1_1");
    c1_1->SetFillColor(kGreen+1);

    TEllipse *el1;
    for (int icircule = 1; icircule < 8; ++icircule) {
        el1 = new TEllipse(0.125*icircule,0.5,.06,.06*90/15);
        el1->SetFillColor(kGreen+2);
        el1->Draw();
    }

    TF1 *radi, *size, *phi;
    radi = new TF1("radi","[0]+x",0.,0.059);
    phi = new TF1("phi","x",0,3.14159*2);
    size = new TF1("size","x",0.01,0.5);
    TMarker *romb;

    for (int icircule = 1; icircule < 8; ++icircule) {
        for (int i = 0; i < Nev_exp[icircule-1]*60; ++i) {
            double iradi = radi->GetRandom();
            double iphi = phi->GetRandom();
            romb= new TMarker(0.125*icircule+iradi*cos(iphi),0.75+iradi*sin(iphi)*90/15,21);
            romb->SetMarkerSize(size->GetRandom());
            romb->SetMarkerColorAlpha(1,1);
            romb->Draw();
        }
    }

    c1->SaveAs("output/rombs.png");
    c1->SaveAs("output/rombs.eps");
    c1->SaveAs("output/rombs.swg");
}


