import sys,os
import itertools
import ROOT
import numpy as np
import math
#from convertColor import convert_color

#ROOT.gROOT.ProcessLine(".x AtlasStyle.C")
#ROOT.gROOT.ProcessLine(".L AtlasLabels.C")
#ROOT.gROOT.ProcessLine("SetAtlasStyle()")

data_file = 'TraceyL1Tree.root'

f = ROOT.TFile.Open(data_file, "read")
t = f.Get("trig")

good_evts = 0
good_l1 = 0
good_hlt = 0

#make empty histograms
c1 = ROOT.TCanvas("c1","c1",800,600)
c1.Divide(2,2)

c2= ROOT.TCanvas("c2","c2",800,600)
c2.Divide(2,2)

c3 = ROOT.TCanvas("c3", "c3", 800, 600)
c3.Divide(2,2)

c4 = ROOT.TCanvas("c4", "c4", 800, 600)
c4.Divide(2,2)

c5= ROOT.TCanvas("c5", "c5", 800, 600)
c5.Divide(2,2)

c6 = ROOT.TCanvas("c6", "c6", 800, 600)
c6.Divide(2,2)

c7 = ROOT.TCanvas("c7", "c7", 800, 600)
c7.Divide(2,2)

c8 = ROOT.TCanvas("c8", "c8", 800, 600)
c8.Divide(2,2)

c9 = ROOT.TCanvas("c9", "c9", 800, 600)
c9.Divide(2,2)

c10 = ROOT.TCanvas("c10","c10", 800, 600)
c10.Divide(2,2)

c11 = ROOT.TCanvas("c11","c11",800,600)
c11.Divide(2,2)

c12 = ROOT.TCanvas("c12","c12",800,600)
c12.Divide(2,2)

c13 = ROOT.TCanvas("c13","c13",800,600)
c13.Divide(2,2)

c14 = ROOT.TCanvas("c14","c14",800,600)
c14.Divide(2,2)

c15 = ROOT.TCanvas("c15","c15",800,600)
c15.Divide(2,2)

c16 = ROOT.TCanvas("c16","c16",800,600)
c16.Divide(2,2)

c17 = ROOT.TCanvas("c17","c17",800,600)
c17.Divide(2,2)

c18 = ROOT.TCanvas("c18","c18",800,600)
c18.Divide(2,2)

c19 = ROOT.TCanvas("c19","c19",800,600)
c19.Divide(2,2)

hHLTwMU4 = ROOT . TH1D (" hHLTwMU4 ", "HLT Trigger Mu24 " ,2 , -0.5, 1.5 )
hL1wMU6 = ROOT . TH1D (" hL1wMU6 ", "L1 Trigger Mu4" ,2 , -0.5, 1.5 )
#hHLTwMU40 = ROOT . TH1D ("hHLTwMU40", "HLT Trigger Mu40" ,2, -0.5,1.5)
#hHLTwMU60 = ROOT . TH1D ("hHLTwMU60", "HLT Trigger Mu60" ,2, -0.5,1.5)
hL1MuPt = ROOT . TH1D (" hL1MuPt","Pt all L1 Mu " , 51 , -0.5 , 25.5 )
hL1MuLen = ROOT . TH1D (" hL1MuLen","L1 number of Muons not passed " , 10 , 0 , 5)
hHLTMuLen =  ROOT . TH1D (" hHLTMuLen","HLT number of Muons not passed " , 10 , 0 , 5)
hHLTMups =  ROOT . TH1D (" hHLTMups","HLT leading failed Muon Pt - 6GeV " , 51 , 0 , 15000)
hL1Mups =  ROOT . TH1D (" hL1Mups","L1 leading failed muon pt - 6GeV" , 51 , 0, 15000)

hMuNum  =  ROOT . TH1D (" hMuNum", "Number of muons per event in total", 10, 0, 5)
hMuEta  =  ROOT . TH1D (" hMuEta", "Value of eta for all leading muons", 20, -6.2, 6.2)
hMuPhi  =  ROOT . TH1D (" hMuPhi", "Value of Phi for all leading muons", 20, -6.2, 6.2)
hMuDR = ROOT . TH1D (" hMuDR", "Value of Delta R for all leading muons", 20, -0.5, 4.5)
hL1Mupass = ROOT . TH1D (" hL1MuPass","L1 leading passing muons pt - 6GeV " , 51 , -0.5 , 25.5 )
hL1Mu10pass = ROOT . TH1D (" hL1Mu10Pass","L1 leading passing muons pt - 10GeV " , 51 , -0.5 , 25.5 )
hL1Mu15pass = ROOT . TH1D (" hL1Mu15Pass","L1 leading passing muons pt - 15GeV " , 51 , -0.5 , 25.5 )
hL12Mu6ps = ROOT . TH1D (" hL12Mu6Ps","L1 leading passing dimuons pt - 6GeV " , 51 , -0.5 , 25.5 )
hL12Mu10ps = ROOT . TH1D (" hL12Mu10Ps","L1 leading passing dimuons pt - 10GeV " , 51 , -0.5 , 25.5 )
hL12Mu20ps = ROOT . TH1D (" hL12Mu20Ps","L1 leading passing dimuons pt - 20GeV " , 51 , -0.5 , 25.5 )

hL1Eff = ROOT . TH1D (" hL1Eff","L1 Efficiency plot - 6GeV" , 51 , -0.5 , 25.5 )
hL1Eff10 = ROOT . TH1D (" hL1Eff10","L1 Efficiency plot - 10GeV" , 51 , -0.5 , 25.5 )
hL1Eff15 = ROOT . TH1D (" hL1Eff15","L1 Efficiency plot - 15GeV " , 51 , -0.5 , 25.5 )
hL1Eff2Mu6 = ROOT . TH1D (" hL1Eff2Mu6","L1 Efficiency plot - dimuon 6GeV" , 51 , -0.5 , 25.5 )
hL1Eff2Mu10 = ROOT . TH1D (" hL1Eff2Mu10","L1 Efficiency plot - dimuon 10GeV" , 51 , -0.5 , 25.5 )
hL1Eff2Mu20 = ROOT . TH1D (" hL1Eff2Mu20","L1 Efficiency plot - dimuon 20GeV" , 51 , -0.5 , 25.5 )

hL1MuDr = ROOT . TH1D (" hL1MuDr", "L1 failed muon Delta R", 62, 0, 6.2)
hHLMuDr = ROOT . TH1D (" hHLMuDr", "HL failed muon Delta R", 62, 0, 6.2)
hL1MuPhi = ROOT . TH1D (" hL1MuPhi", "Delta Phi of Leading passing muon -6GeV L1", 62, -6.2, 6.2)
hHLMuPhi = ROOT . TH1D (" hHLMuPhi", "Delta Phi of Leading passing muon -6GeV HL", 62, -6.2, 6.2)

hInMass = ROOT . TH1D (" hInMass", "calculated invariant mass of muons - 6GeV",  51 , -0.5 , 25.5 )
hInMassAll = ROOT . TH1D (" hInMassAll", "calculated invariant mass of All muons",  51 , -0.5 , 25.5 )
hInMassAll2 = ROOT . TH1D (" hInMassAll2", "calculated invariant mass of muons",  51 , -0.5 , 85.5 )
hInMass2 = ROOT . TH1D (" hInMass2", "calculated invariant mass of muons",  51 , -0.5 , 85.5 )
hInMass78 = ROOT . TH1D (" hInMass78", "calculated invariant mass of muons <78",  51 , -0.5 , 85.5 )
hInMass10 = ROOT . TH1D (" hInMass10", "calculated invariant mass of muons - 10GeV",  51 , -0.5 , 25.5 )
hInMass102 = ROOT . TH1D (" hInMass102", "calculated invariant mass of muons",  51 , -0.5 , 85.5 )
hInMass1078 = ROOT . TH1D (" hInMass1078", "calculated invariant mass of muons <78",  51 , -0.5 , 85.5 )
hInMass15 = ROOT . TH1D (" hInMass15", "calculated invariant mass of muons - 15GeV",  51 , -0.5 , 25.5 )
hInMass152 = ROOT . TH1D (" hInMass152", "calculated invariant mass of muons",  51 , -0.5 , 85.5 )
hInMass1578 = ROOT . TH1D (" hInMass1578", "calculated invariant mass of muons <78",  51 , -0.5 , 85.5 )
hInMass20 = ROOT . TH1D (" hInMass20", "calculated invariant mass of muons - 20GeV",  51 , -0.5 , 25.5 )
hInMass202 = ROOT . TH1D (" hInMass202", "calculated invariant mass of muons",  51 , -0.5 , 85.5 )
hInMass2078 = ROOT . TH1D (" hInMass2078", "calculated invariant mass of muons <78",  51 , -0.5 , 85.5 )
hInMass2Mu6 = ROOT . TH1D (" hInMass2Mu6", "calculated invariant mass of dimuons - 6GeV",  51 , -0.5 , 85.5 )
hInMass2Mu678 = ROOT . TH1D (" hInMass2Mu678", "calculated invariant mass of dimuons <78",  51 , -0.5 , 85.5 )
hInMass2Mu10 = ROOT . TH1D (" hInMass2Mu10", "calculated invariant mass of dimuons - 10GeV",  51 , -0.5 , 85.5 )
hInMass2Mu1078 = ROOT . TH1D (" hInMass2Mu1078", "calculated invariant mass of dimuons <78",  51 , -0.5 , 85.5 )
hInMass2Mu20 =  ROOT . TH1D (" hInMass2Mu20", "calculated invariant mass of dimuons - 20GeV",  51 , -0.5 , 85.5 )
hInMass2Mu2078 = ROOT . TH1D (" hInMass2Mu2078", "calculated invariant mass of dimuons <78",  51 , -0.5 , 85.5 )

hRecInMass = ROOT . TH1D (" hRecInMass", "Calculated invariant mass of reconstructed muons -6GeV", 50, -0.5, 25.5)
hRecInMass2 = ROOT . TH1D (" hRecInMass2", "Calculated invariant mass of reconstructed muons", 50, 0, 85.5)
hRecInMass78 = ROOT . TH1D (" hRecInMass78", "Calculated invariant mass of reconstructed muons >78GeV", 50, 0, 85.5)
hRecAllInMass = ROOT . TH1D (" hRecAllInMass", "Calculated invariant mass of All reconstructed muons", 50, 0, 85.5)
hRecInMass10 = ROOT . TH1D (" hRecInMass10", "Calculated invariant mass of reconstructed muons - 10GeV", 50, 0, 85.5)
#hRecInMass102 = ROOT . TH1D (" hRecInMass102", "Calculated invariant mass of reconstructed muons", 50, 0, 85.5)
hRecInMass1078 = ROOT . TH1D (" hRecInMass1078", "Calculated invariant mass of reconstructed muons >78GeV", 50, 0, 85.5)
hRecInMass14 = ROOT . TH1D (" hRecInMass14", "Calculated invariant mass of reconstructed muons - 15GeV", 50, 0, 85.5)
#hRecInMass142 = ROOT . TH1D (" hRecInMass142", "Calculated invariant mass of reconstructed muons", 50, 0, 85.5)
hRecInMass1478 = ROOT . TH1D (" hRecInMass1478", "Calculated invariant mass of reconstructed muons >78GeV", 50, 0, 85.5)
hRecInMass20 = ROOT . TH1D (" hRecInMass20", "Calculated invariant mass of reconstructed muons - 20GeV", 50, 0, 85.5)
#hRecInMass202 = ROOT . TH1D (" hRecInMass202", "Calculated invariant mass of reconstructed muons", 50, 0, 85.5)
hRecInMass2078 = ROOT . TH1D (" hRecInMass2078", "Calculated invariant mass of reconstructed muons >78GeV", 50, 0, 85.5)

hRecInMass2Mu6 = ROOT . TH1D (" hRecInMass2Mu6", "Calculated invariant mass of reconstructed muons - 6GeV dimuon", 50, 0, 85.5)
hRecInMass2Mu678 = ROOT . TH1D (" hRecInMass2Mu678", "Calculated invariant mass of reconstructed muons - 6GeV dimuon <78", 50, 0, 85.5)
hRecInMass2Mu10 = ROOT . TH1D (" hRecInMass2Mu10", "Calculated invariant mass of reconstructed muons - 10GeV dimuon", 50, 0, 85.5)
hRecInMass2Mu1078 = ROOT . TH1D (" hRecInMass2Mu1078", "Calculated invariant mass of reconstructed muons - 10GeV dimuon <78", 50, 0, 85.5)
hRecInMass2Mu14 = ROOT . TH1D (" hRecInMass2Mu14", "Calculated invariant mass of reconstructed muons - 14GeV dimuon", 50, 0, 85.5)
hRecInMass2Mu1478 = ROOT . TH1D (" hRecInMass2Mu1478", "Calculated invariant mass of reconstructed muons - 14GeV dimuon <78", 50, 0, 85.5)
hRecInMass2Mu20 = ROOT . TH1D (" hRecInMass2Mu20", "Calculated invariant mass of reconstructed muons - 20GeV dimuon", 50, 0, 85.5)

#hRecMups =  ROOT . TH1D (" hRecMuLen","L1 first failed muon pt " , 51 , 0, 15000)
hRecMulen  =  ROOT . TH1D (" hRecLen", "Rec Number of muons per event in total", 10, -0.5, 9.5)
hRecMups = ROOT . TH1D (" hRecMups", "Rec Muon Leading Pt ", 50, 0, 50)
hRecL1Mupass = ROOT . TH1D (" hRecL1Mupass", "Rec Leading passing muon Pt -6GeV ", 50, 0, 50)
hRecL1Mu10pass = ROOT . TH1D (" hRecL1Mu10pass", "Rec Leading passing muon Pt - 10GeV ", 50, 0, 50)
hRecL1Mu14pass = ROOT . TH1D (" hRecL1Mu14pass", "Rec Leading passing muon Pt - 14GeV", 50, 0, 50)
hRecL12Mu6pass = ROOT . TH1D (" hRecL12Mu6pass", "Rec Leading passing muon Pt -6GeV ", 50, 0, 50)
hRecL12Mu10pass = ROOT . TH1D (" hRecL12Mu10pass", "Rec Leading passing muon Pt - 10GeV ", 50, 0, 50)
hRecL12Mu14pass = ROOT . TH1D (" hRecL12Mu14pass", "Rec Leading passing muon Pt - 14GeV", 50, 0, 50)
hRecL1Eff = ROOT . TH1D (" hRecL1Eff", "Rec L1 Efficiency Plot - 6GeV ", 50, 0, 50)
hRecL1Eff10 = ROOT . TH1D (" hRecL1Eff10", "Rec L1 efficiency Plot - 10 GeV ", 50, 0, 50)
hRecL1Eff14 = ROOT . TH1D (" hRecL1Eff14", "Rec L1 efficiency Plot - 14GeV ", 50, 0, 50)
hRecL1Eff2mu6 = ROOT . TH1D (" hRecL1Eff2mu6", "Rec L1 Efficiency Plot - 6GeV ", 50, 0, 50)
hRecL1Eff2mu10 = ROOT . TH1D (" hRecL1Eff2mu10", "Rec L1 efficiency Plot - 10 GeV ", 50, 0, 50)
hRecL1Eff2mu14 = ROOT . TH1D (" hRecL1Eff2mu14", "Rec L1 efficiency Plot - 14GeV ", 50, 0, 50)

hRecL1Mups =  ROOT . TH1D (" hRecL1Mups","Rec L1 failed muon pt " , 51 , 0, 15000)
hRecL1Mulen  =  ROOT . TH1D (" hRecL1Mulen", "Rec Number of muons per event in total", 10, 0, 5)
hRecHLTMups = ROOT . TH1D (" hRecHLTMups", "Rec HLT leading failed muon pt", 10, 0, 15000)
hRecL1Mulen = ROOT . TH1D (" hRecL1Mulen", "Number of muons per event in total", 10, 0, 5)

hRecMuDR = ROOT . TH1D (" hRecMuDR", "Rec Delta R", 62, -0.5, 6.5)
hRecHLTMuDRFailMu6 = ROOT . TH1D (" hRecHLTDRFailMu6", "Rec HLT Delta R Mu 6", 62, 0, 6.2)
hRecHLMuPhi = ROOT . TH1D (" hRecHLMuPhi", "Delta Phi of Leading passing Rec muon -6GeV HL", 62, -6.2, 6.2)
hRecL1MuPhi = ROOT . TH1D (" hRecL1MuPhi", "Delta Phi of Leading passing Rec muon -6GeV L1", 62, -6.2, 6.2)

hRecMuEta  =  ROOT . TH1D (" hRecMuEta", "Value of eta for all leading Rec muons", 20, -6.2, 6.2)
hRecMuPhi  =  ROOT . TH1D (" hRecMuPhi", "Value of Phi for all leading Rec muons", 20, -6.2, 6.2)

hMassEff= ROOT.TH1D("hRecMassEff","Rec Invariant mass vs Rate", 51 , -0.5 , 80 )
hMassEff78 = ROOT.TH1D("hMassEff78","Rec Invariant mass vs Rate", 51 , -0.5 , 80 )    
hMassEff10 = ROOT.TH1D("hMassEff10","Rec Invariant mass vs Rate", 51 , -0.5 , 80 )
hMassEff15 = ROOT.TH1D("hMassEff15","Rec Invariant mass vs Rate", 51 , -0.5 , 80 )
hMassEff20 = ROOT.TH1D("hMassEff20","Rec Invariant mass vs Rate", 51 , -0.5 , 80 )
hMassEff1078 = ROOT.TH1D("hMassEff1078","Rec Invariant mass vs Rate", 51 , -0.5 , 80 )
hMassEff1578 = ROOT.TH1D("hMassEff1578","Rec Invariant mass vs Rate", 51 , -0.5 , 80 )
hMassEff2078 = ROOT.TH1D("hMassEff2078","Rec Invariant mass vs Rate", 51 , -0.5 , 80 )

hMassEff2Mu6 = ROOT.TH1D("hMassEff2Mu6","Rec Invariant mass vs Rate- 6GeV dimuon", 51 , -0.5 , 80 )
hMassEff2Mu10 = ROOT.TH1D("hMassEff2Mu10","Rec Invariant mass vs Rate- 10GeV dimuon", 51 , -0.5 , 80 )
hMassEff2Mu20 = ROOT.TH1D("hMassEff2Mu20","Rec Invariant mass vs Rate- 20GeV dimuon", 51 , -0.5 , 80 )
hMassEff2Mu678 = ROOT.TH1D("hMassEff2Mu678","Rec Invariant mass vs Rate- 6GeV dimuon <78", 51 , -0.5 , 80 )
hMassEff2Mu1078 = ROOT.TH1D("hMassEff2Mu1078","Rec Invariant mass vs Rate- 10GeV dimuon <78", 51 , -0.5 , 80 )
hMassEff2Mu2078 = ROOT.TH1D("hMassEff2Mu2078","Rec Invariant mass vs Rate- 20GeV dimuon <78", 51 , -0.5 , 80 )

hRecMassEff = ROOT.TH1D("hRecMassEff","Rec Invariant mass vs Rate",50,0,80)
hRecMassEff78 = ROOT.TH1D("hRecMassEff78","Rec Invariant mass vs Rate",50,0,80)
hRecMassEff10 = ROOT.TH1D("hRecMassEff10","Rec Invariant mass vs Rate",50,0,80)
hRecMassEff14 = ROOT.TH1D("hRecMassEff14","Rec Invariant mass vs Rate",50,0,80)
hRecMassEff20 = ROOT.TH1D("hRecMassEff20","Rec Invariant mass vs Rate",50,0,80)
hRecMassEff1078 = ROOT.TH1D("hRecMassEff1078","Rec Invariant mass vs Rate",50,0,80)
hRecMassEff1478 = ROOT.TH1D("hRecMassEff1478","Rec Invariant mass vs Rate",50,0,80)
hRecMassEff2078 = ROOT.TH1D("hRecMassEff2078","Rec Invariant mass vs Rate",50,0,80)

hEtaLead = ROOT.TH1D("hEtaLead","Value of leading eta - dimuon 6GeV",50,-6.2,6.2)
hEtaSub = ROOT.TH1D("hEtaSub","Value of subbing eta - dimuon 6GeV",50,-6.2,6.2)
hDeltaEta = ROOT.TH1D("hDeltaEta","Difference in eta for leading and subleading muons - dimuon",50,-6.2,6.2)
hEtaLen = ROOT.TH1D("hEtaLen","number of muons passing 6GeV dimuons trigger with delta eta between 2 and Pi",10,0,5)

#loop over the events in the tree 
#ie = iterator over the events
for ie,event in enumerate(t):
    if(ie % 100000 == 0): print ('event: ',ie)
    passtrigHLmu6 = event.HLT_mu6
    passtrigHLmu10 = event.HLT_mu10
    passtrigHLmu14 = event.HLT_mu14
    passtrigHLmu20 = event.HLT_mu20
    passtrigHL2mu4 = event.HLT_2mu4
    passtrigHL2mu6 = event.HLT_2mu6
    passtrigHL2mu10 = event.HLT_2mu10
    passtrigHL2mu14 = event.HLT_2mu14
    passtrigL1mu6= event.L1_MU6
    passtrigL1mu10 = event.L1_MU10
    passtrigL1mu15 = event.L1_MU15
    passtrigL1mu20 = event.L1_MU20
    passtrigL12mu4 = event.L1_2MU4
    passtrigL12mu6 = event.L1_2MU6
    passtrigL12mu10 = event.L1_2MU10
    passtrigL12mu20 = event.L1_2MU20_OVERLAY
        
    #Fill histograms
    hHLTwMU4.Fill ( passtrigHLmu6 )
    hL1wMU6.Fill ( passtrigL1mu6 )
#    hHLTwMU40.Fill ( passtrigHLmu40 )
#    hHLTwMU60.Fill ( passtrigHLmu60 )
    
    #increase counters
    good_evts = good_evts + 1
    good_l1 = good_l1 + 1
  #  good_hlt = good_hlt + passhlt
    
    
       #look at L1 muons 
    #get the reco muons and the L1 Muon RoIs
    #l1 list is already sorted!
    l1muons_vec = event.l1muons
    if len(l1muons_vec)>0:
      hL1MuPt.Fill (l1muons_vec[0].Pt() / 1000)
      
    i = 0
    l1muons=[]
    for l1mu in l1muons_vec: 
      if l1mu.Pt() > 1:
        l1muons.append( l1mu)
#        print(i, l1muons[i])
        i=i+1
#Filling baseline histograms before triggers
    hMuNum.Fill (len(l1muons))
    if len(l1muons)>0:
      hMuEta.Fill(l1muons_vec[0].Eta())
      hMuPhi.Fill(l1muons_vec[0].Phi())
#      hL1MuPt.Fill (l1muons_vec[0].Pt() / 1000)
    if len(l1muons) >1:
      L1muons=  (l1muons_vec[0]+l1muons_vec[1]).M()*0.001
      hMuDR.Fill(l1muons_vec[0].DeltaR(l1muons_vec[1]))
      hInMassAll.Fill((l1muons_vec[0]+l1muons_vec[1]).M()*0.001 )
      hInMassAll2.Fill((l1muons_vec[0]+l1muons_vec[1]).M()*0.001 )
      DeltaEta = l1muons_vec[0].Eta()-l1muons_vec[1].Eta()
    if len(l1muons) > 0 and passtrigL1mu10:
      hL1Mu10pass.Fill(l1muons_vec[0].Pt() / 1000)
    
    if len(l1muons) > 0 and passtrigL1mu15:
      hL1Mu15pass.Fill(l1muons_vec[0].Pt() / 1000)  
        
    if len(l1muons) > 0 and passtrigL1mu6:
      hL1Mupass.Fill(l1muons_vec[0].Pt() / 1000)
      
    if len(l1muons) > 1 and passtrigL1mu6:
      hL1MuPhi.Fill(l1muons_vec[0].DeltaPhi(l1muons[1]))
      if abs(l1muons_vec[0].DeltaPhi(l1muons[1])) < 0.2:
        print("leading eta, Pt, Phi", l1muons_vec[0].Eta(), l1muons_vec[0].Pt(), l1muons_vec[0].Phi())
        print("second eta, Pt, phi", l1muons_vec[1].Eta(), l1muons_vec[1].Pt(), l1muons_vec[1].Phi())
      hInMass.Fill((l1muons_vec[0]+l1muons_vec[1]).M()*0.001 )
      hInMass2.Fill((l1muons_vec[0]+l1muons_vec[1]).M()*0.001 )
      if L1muons>12 and L1muons<78:
        hInMass78.Fill(L1muons)

    if len(l1muons) > 1 and passtrigL1mu10:
      hInMass10.Fill(L1muons)
      hInMass102.Fill(L1muons)
      if L1muons>12 and L1muons<78:
        hInMass1078.Fill(L1muons)
   
   
    if len(l1muons) >1 and passtrigL1mu15:
      hInMass15.Fill(L1muons)
      hInMass152.Fill(L1muons)
      if L1muons>12 and L1muons<78:
        hInMass1578.Fill(L1muons)
        
    if len(l1muons) >1 and passtrigL1mu20:
      hInMass20.Fill(L1muons)
      hInMass202.Fill(L1muons)
      if L1muons>12 and L1muons<78:
        hInMass2078.Fill(L1muons)
 
#dimuons triggers
        
    if len(l1muons) >0 and passtrigL12mu6:
      hL12Mu6ps.Fill(l1muons_vec[0].Pt()/1000)
    if len(l1muons) >1 and passtrigL12mu6:
      hEtaLead.Fill(l1muons_vec[0].Eta())
      hEtaSub.Fill(l1muons_vec[1].Eta())
      hDeltaEta.Fill(DeltaEta)
      if abs(DeltaEta)>2 and abs(DeltaEta)<math.pi:
        hEtaLen.Fill(len(l1muons))
      hInMass2Mu6.Fill(L1muons)
      if L1muons>12 and L1muons<78:
        hInMass2Mu678.Fill(L1muons)      
    
    if len(l1muons)>0 and passtrigL12mu10:
      hL12Mu10ps.Fill(l1muons_vec[0].Pt()/1000)
    if len(l1muons)>1 and passtrigL12mu10:
      hInMass2Mu10.Fill(L1muons)
      if L1muons>12 and L1muons<78:
        hInMass2Mu1078.Fill(L1muons)
        
    if len(l1muons)>0 and passtrigL12mu20:
      hL12Mu20ps.Fill(l1muons_vec[0].Pt()/1000)
    if len(l1muons)>1 and passtrigL12mu20:
      hInMass2Mu20.Fill(L1muons)
      if L1muons>12 and L1muons<78:
        hInMass2Mu2078.Fill(L1muons)    
              
    if len(l1muons) >1 and passtrigHLmu6:
      hHLMuPhi.Fill(l1muons_vec[0].DeltaPhi(l1muons[1]))
          
    if len(l1muons) > 0 and not passtrigHLmu6:
           # if i>1:
           #  hHLMuDr.Fill(l1muons[0].DeltaR(l1muons[1]))
  #      print ("Pt of first muon in event", l1muons_vec[0].Pt())
      hHLTMuLen.Fill(len(l1muons))
      hHLTMups.Fill(l1muons_vec[0].Pt())
    
    
    if len(l1muons) > 0 and not passtrigL1mu6:
      hL1Mups.Fill (l1muons_vec[0].Pt())
      hL1MuLen.Fill(len(l1muons))
           # if len(l1muons) > 1:
            #  hL1MuDr.Fill( l1muons[0].DeltaR(l1muons[1]))
#        print ("number of failing muons=", len(l1muons))
#        print ("Pt of first muon in event", l1muons_vec[0].Pt())

 #Dividing histograms to make efficiency plots       
    hL1Eff = hL1Mupass.Clone()
    hL1Eff.Divide(hL1MuPt)
    
    hL1Eff10 = hL1Mu10pass.Clone()
    hL1Eff10.Divide(hL1MuPt)
    
    hL1Eff15 = hL1Mu15pass.Clone()
    hL1Eff15.Divide(hL1MuPt)
    
    hL1Eff2Mu6 = hL12Mu6ps.Clone()
    hL1Eff2Mu6.Divide(hL1MuPt)
    
    hL1Eff2Mu10 = hL12Mu10ps.Clone()
    hL1Eff2Mu10.Divide(hL1MuPt)  
    
    hL1Eff2Mu20 = hL12Mu20ps.Clone()
    hL1Eff2Mu20.Divide(hL1MuPt)       
    
    hMassEff = hInMass2.Clone()
    hMassEff.Divide(hInMassAll2)
        
    hMassEff78 = hInMass78.Clone()
    hMassEff78.Divide(hInMassAll2)    
    
    hMassEff10 = hInMass102.Clone()
    hMassEff10.Divide(hInMassAll2)
    
    hMassEff15 = hInMass152.Clone()
    hMassEff15.Divide(hInMassAll2)
    
    hMassEff20 = hInMass202.Clone()
    hMassEff20.Divide(hInMassAll2)
    
    hMassEff1078 = hInMass1078.Clone()
    hMassEff1078.Divide(hInMassAll2)
    
    hMassEff1578 = hInMass1578.Clone()
    hMassEff1578.Divide(hInMassAll2)
    
    hMassEff2078 = hInMass2078.Clone()
    hMassEff2078.Divide(hInMassAll2)
    
    hMassEff2Mu6 = hInMass2Mu6.Clone()
    hMassEff2Mu6.Divide(hInMassAll2)
        
    hMassEff2Mu678 = hInMass2Mu678.Clone()
    hMassEff2Mu678.Divide(hInMassAll2)    
    
    hMassEff2Mu10 = hInMass2Mu10.Clone()
    hMassEff2Mu10.Divide(hInMassAll2)

    hMassEff2Mu20 = hInMass2Mu20.Clone()
    hMassEff2Mu20.Divide(hInMassAll2)
    
    hMassEff2Mu1078 = hInMass2Mu1078.Clone()
    hMassEff2Mu1078.Divide(hInMassAll2)
    
    hMassEff2Mu2078 = hInMass2078.Clone()
    hMassEff2Mu2078.Divide(hInMassAll2) 
    
    hEtaEff = hEtaLen.Clone()
    hEtaEff.Divide(hMuNum)          
#    if len(l1muons) > 1 and passtrigHLmu4 and len(pair_indices) < 2:
#        print ('two muons, HLT, L1, but not matched')
  
 #repeat for reconstructed muons with high level triggers          
    recomuons_vec = event.recomuons
    recomuons = [mu for mu in recomuons_vec if mu.Pt() > 1]
    recomuons.sort(key=lambda mu: mu.Pt(), reverse=True)
  
    hRecMulen.Fill(len(recomuons))
    if len(recomuons)>0:
      hRecMuEta.Fill(recomuons_vec[0].Eta())
      hRecMuPhi.Fill(recomuons_vec[0].Phi())
      hRecMups.Fill(recomuons_vec[0].Pt() / 1000)
    if len(recomuons) > 1:
      hRecMuDR.Fill(recomuons[0].DeltaR(recomuons[1])) 
      
    if len(recomuons) > 1 and passtrigHLmu6:
      hRecHLMuPhi.Fill(recomuons[0].DeltaPhi(recomuons[1]))  
    
    if len(recomuons) > 1 and not passtrigHLmu6:
  #      print( "recovered delta R HLT=", recomuons[0].DeltaR(recomuons[1]))
      hRecHLTMuDRFailMu6.Fill(recomuons[0].DeltaR(recomuons[1])) 
    if len(recomuons)> 1:  
      recoM=(recomuons_vec[0]+recomuons_vec[1]).M()*0.001
      hRecAllInMass.Fill(recoM)
    
    if len(recomuons) > 1 and passtrigHLmu6:
      hRecL1Mupass.Fill(recomuons_vec[0].Pt() / 1000)
      hRecL1MuPhi.Fill(recomuons_vec[0].DeltaPhi(recomuons[1]))
      hRecInMass.Fill((recomuons_vec[0]+recomuons_vec[1]).M()*0.001 )
      hRecInMass2.Fill((recomuons_vec[0]+recomuons_vec[1]).M()*0.001 )
      if recoM > 12 and recoM < 78:
        hRecInMass78.Fill((recomuons_vec[0]+recomuons_vec[1]).M()*0.001)
  
    if len(recomuons) > 0 and passtrigHLmu10:
      hRecL1Mu10pass.Fill(recomuons_vec[0].Pt() / 1000)
    if len(recomuons) >1 and passtrigHLmu10:
      hRecInMass10.Fill(recoM)
      if recoM > 12 and recoM < 78:
        hRecInMass1078.Fill(recoM)
   
    if len(recomuons) > 0 and passtrigHLmu14:
        hRecL1Mu14pass.Fill(recomuons_vec[0].Pt() / 1000)
   
    if len(recomuons) >1 and passtrigHLmu14:
      hRecInMass14.Fill(recoM)
      if recoM > 12 and recoM < 78:
        hRecInMass1478.Fill(recoM)
      
    if len(recomuons) >1 and passtrigHLmu20:
      hRecInMass20.Fill(recoM)
      if recoM > 12 and recoM < 78:
        hRecInMass2078.Fill(recoM)
                 
    if len(recomuons) > 0 and passtrigHL2mu6:
      hRecL12Mu6pass.Fill(recomuons_vec[0].Pt()/1000)
    if len(recomuons) > 1 and passtrigHL2mu6:
      hRecInMass2Mu6.Fill(recoM)
      if recoM > 12 and recoM <78:
        hRecInMass2Mu678.Fill(recoM)

  
    if len(recomuons) > 0 and passtrigHL2mu10:
      hRecL12Mu10pass.Fill(recomuons_vec[0].Pt() / 1000)
    if len(recomuons) >1 and passtrigHL2mu10:
      hRecInMass2Mu10.Fill(recoM)
      if recoM > 12 and recoM < 78:
        hRecInMass2Mu1078.Fill(recoM)
   
    if len(recomuons) > 0 and passtrigHL2mu14:
        hRecL12Mu14pass.Fill(recomuons_vec[0].Pt() / 1000)
   
    if len(recomuons) >1 and passtrigHL2mu14:
      hRecInMass2Mu14.Fill(recoM)
      if recoM > 12 and recoM < 78:
        hRecInMass2Mu1478.Fill(recoM)
      
                     
    if len(recomuons) > 1 and not passtrigHLmu6:
#        print("recovered delta R L1=",  recomuons[0].DeltaR(recomuons[1]))
        hRecL1Mups.Fill(recomuons_vec[0].Pt())
        hRecL1Mulen.Fill(len(recomuons))
 #       print ('two muons, no L1')
    
      
    hRecL1Eff=hRecL1Mupass.Clone()
    hRecL1Eff.Divide(hRecMups)
    
    hRecL1Eff10=hRecL1Mu10pass.Clone()
    hRecL1Eff10.Divide(hRecMups)
    
    hRecL1Eff14=hRecL1Mu14pass.Clone()
    hRecL1Eff14.Divide(hRecMups)
    
    hRecL1Eff2mu6=hRecL12Mu6pass.Clone()
    hRecL1Eff2mu6.Divide(hRecMups)
    
    hRecL1Eff2mu10=hRecL12Mu10pass.Clone()
    hRecL1Eff2mu10.Divide(hRecMups)
    
    hRecL1Eff2mu14=hRecL12Mu14pass.Clone()
    hRecL1Eff2mu14.Divide(hRecMups)
    
    hRecMassEff=hRecInMass2.Clone()
    hRecMassEff.Divide(hRecAllInMass)
    
    hRecMassEff78=hRecInMass78.Clone()
    hRecMassEff78.Divide(hRecAllInMass)
    
    hRecMassEff10=hRecInMass10.Clone()
    hRecMassEff10.Divide(hRecAllInMass)
    
    hRecMassEff1078=hRecInMass1078.Clone()
    hRecMassEff1078.Divide(hRecAllInMass)
    
    hRecMassEff14=hRecInMass14.Clone()
    hRecMassEff14.Divide(hRecAllInMass)
    
    hRecMassEff1478=hRecInMass1478.Clone()
    hRecMassEff1478.Divide(hRecAllInMass)
    
    hRecMassEff20=hRecInMass20.Clone()
    hRecMassEff20.Divide(hRecAllInMass)
    
    hRecMassEff2078=hRecInMass2078.Clone()
    hRecMassEff2078.Divide(hRecAllInMass)
    
    hRecMassEff2Mu6=hRecInMass2Mu6.Clone()
    hRecMassEff2Mu6.Divide(hRecAllInMass)
    
    hRecMassEff2Mu678=hRecInMass2Mu678.Clone()
    hRecMassEff2Mu678.Divide(hRecAllInMass)
    
    hRecMassEff2Mu10=hRecInMass2Mu10.Clone()
    hRecMassEff2Mu10.Divide(hRecAllInMass)
    
    hRecMassEff2Mu1078=hRecInMass2Mu1078.Clone()
    hRecMassEff2Mu1078.Divide(hRecAllInMass)
    
    hRecMassEff2Mu14=hRecInMass2Mu14.Clone()
    hRecMassEff2Mu14.Divide(hRecAllInMass)
    
    hRecMassEff2Mu1478=hRecInMass2Mu1478.Clone()
    hRecMassEff2Mu1478.Divide(hRecAllInMass)

    
 #   if len(recomuons) > 1 and passhlt and len(pair_indices) < 2:
 #       print ('two muons, HLT, L1, but not matched')
   
print (" iterator starts from 0, so add 1 for number of events!") 
print (good_evts ,'/',ie)
print (good_l1 ,'/',ie)
print (good_hlt ,'/',ie)

#make plots pretty!
#hHLTwMU4.SetLineColor(2)
#hHLTwMU4.SetFillColor(2)
#hHLTwMU4.SetFillStyle(3004)

#hHLTwMU6.SetLineColor(8)
#hHLTwMU6.SetFillColor(8)
#hHLTwMU6.SetFillStyle(3004)

#hHLTwMU10.SetLineColor(9)
#hHLTwMU10.SetFillColor(9)
#hHLTwMU10.SetFillStyle(3004)

#hHLTwMU60.SetLineColor(1)
#hHLTwMU60.SetFillColor(1)
#hHLTwMU60.SetFillStyle(3004)


hL1Eff.SetTitle("L1 Efficiency Plot - 6GeV")
hL1Eff.GetXaxis().SetTitle("Pt /GeV")
hL1Eff.GetYaxis().SetTitle("Efficiency")
hL1Eff.SetMarkerStyle(22)
#hL1Eff.SetMarkerColor(convert_color(col,'root'))


hRecL1Eff.SetTitle(" Rec L1 Efficiency Plot - 6GeV")
hRecL1Eff.GetXaxis().SetTitle("Pt /GeV")
hRecL1Eff.GetYaxis().SetTitle("Efficiency")
hRecL1Eff.SetMarkerStyle(22)

hL1Eff10.SetTitle("L1 Efficiency Plot - 10GeV")
hL1Eff10.GetXaxis().SetTitle("Pt /GeV")
hL1Eff10.GetYaxis().SetTitle("Efficiency")
hL1Eff10.SetMarkerStyle(22)
#hL1Eff.SetMarkerColor(convert_color(col,'root'))


hRecL1Eff10.SetTitle(" Rec L1 Efficiency Plot - 10GeV")
hRecL1Eff10.GetXaxis().SetTitle("Pt /GeV")
hRecL1Eff10.GetYaxis().SetTitle("Efficiency")
hRecL1Eff10.SetMarkerStyle(22)

hL1Eff15.SetTitle("L1 Efficiency Plot - 15GeV")
hL1Eff15.GetXaxis().SetTitle("Pt /GeV")
hL1Eff15.GetYaxis().SetTitle("Efficiency")
hL1Eff15.SetMarkerStyle(22)
#hL1Eff.SetMarkerColor(convert_color(col,'root'))


hRecL1Eff14.SetTitle(" Rec L1 Efficiency Plot - 14GeV")
hRecL1Eff14.GetXaxis().SetTitle("Pt /GeV")
hRecL1Eff14.GetYaxis().SetTitle("Efficiency")
hRecL1Eff14.SetMarkerStyle(22)

hMassEff.SetTitle("Mass vs Rate - 6GeV")
hMassEff.GetXaxis().SetTitle("Invariant Mass/GeV")
hMassEff.GetYaxis().SetTitle("rate")
hMassEff.SetMarkerStyle(22)

hRecMassEff.SetTitle("Rec Invariant Mass vs rate - 6GeV")
hRecMassEff.GetXaxis().SetTitle("Pt /GeV")
hRecMassEff.GetYaxis().SetTitle("rate")
hRecMassEff.SetMarkerStyle(22)

hInMass.SetTitle("Invariant mass of muons - 6GeV")
hInMass.GetXaxis().SetTitle("Invariant mass /GeV")
hInMass.GetYaxis().SetTitle("Efficiency")
hInMass.SetMarkerStyle(22)

hRecInMass.SetTitle("Rec muon invariant mass - 6GeV")
hRecInMass.GetXaxis().SetTitle("Invariant mass / GeV")
hRecInMass.GetYaxis().SetTitle("Efficiency")
hRecInMass.SetMarkerStyle(22)

hL1Mupass.GetXaxis().SetTitle("Pt / GeV")
hL1Mupass.GetYaxis().SetTitle("Number of muons")
hL1Mupass.SetMarkerStyle(22)

hL1MuPt.GetXaxis().SetTitle("Pt / Gev")
hL1MuPt.GetYaxis().SetTitle("number of muons")
hL1MuPt.SetMarkerStyle(22)

hRecMups.GetXaxis().SetTitle("Pt / Gev")
hRecMups.GetYaxis().SetTitle("number of muons")
hRecMups.SetMarkerStyle(22)

hL1MuPt.GetXaxis().SetTitle("Pt / Gev")
hL1MuPt.GetYaxis().SetTitle("number of muons")
hL1MuPt.SetMarkerStyle(22)

hL1Mu15pass.GetXaxis().SetTitle("Pt / Gev")
hL1Mu15pass.GetYaxis().SetTitle("number of muons")
hL1Mu15pass.SetMarkerStyle(22)

hL1Mu10pass.GetXaxis().SetTitle("Pt / Gev")
hL1Mu10pass.GetYaxis().SetTitle("number of muons")
hL1Mu10pass.SetMarkerStyle(22)

hEtaEff.SetTitle("Number of muons in Eta peak vs Number of All Muons")

hHLTMups.SetLineColor(1)
hHLTMups.SetFillColor(1)
hHLTMups.SetFillStyle(3004)

hL1Mups.SetLineColor(2)
hL1Mups.SetFillColor(2)
hL1Mups.SetFillStyle(3004)

hL1MuPt.SetLineColor(3)
hL1MuPt.SetFillColor(3)
hL1MuPt.SetFillStyle(3004)

hHLTMuLen.SetLineColor(8)
hHLTMuLen.SetFillColor(8)
hHLTMuLen.SetFillStyle(3004)

hL1MuLen.SetLineColor(9)
hL1MuLen.SetFillColor(9)
hL1MuLen.SetFillStyle(3004)

hRecMulen.SetLineColor(1)
hRecMulen.SetFillColor(1)
hRecMulen.SetFillStyle(3004)

hRecMups.SetLineColor(2)
hRecMups.SetFillColor(2)
hRecMups.SetFillStyle(3004)

hRecMuDR.SetLineColor(3)
hRecMuDR.SetFillColor(3)
hRecMuDR.SetFillStyle(3004)

hRecHLTMuDRFailMu6.SetLineColor(9)
hRecHLTMuDRFailMu6.SetFillColor(9)
hRecHLTMuDRFailMu6.SetFillStyle(3004)

hL1Eff.SetLineColor(9)
hL1Eff.SetFillColor(9)
hL1Eff.SetFillStyle(3004)

hRecL1Eff.SetLineColor(4)
hRecL1Eff.SetFillColor(4)
hRecL1Eff.SetFillStyle(3004)

hL1Eff10.SetLineColor(9)
hL1Eff10.SetFillColor(9)
hL1Eff10.SetFillStyle(3004)

hRecL1Eff10.SetLineColor(4)
hRecL1Eff10.SetFillColor(4)
hRecL1Eff10.SetFillStyle(3004)

hL1Eff15.SetLineColor(9)
hL1Eff15.SetFillColor(9)
hL1Eff15.SetFillStyle(3004)

hRecL1Eff14.SetLineColor(4)
hRecL1Eff14.SetFillColor(4)
hRecL1Eff14.SetFillStyle(3004)

hMuEta.SetLineColor(1)
hMuEta.SetFillColor(1)
hMuEta.SetFillStyle(3004)

hMuPhi.SetLineColor(2)
hMuPhi.SetFillColor(2)
hMuPhi.SetFillStyle(3004)

hMuDR.SetLineColor(9)
hMuDR.SetFillColor(9)
hMuDR.SetFillStyle(3004)

hInMass.SetLineColor(1)
hInMass.SetFillColor(1)
hInMass.SetFillStyle(3004)

hRecInMass.SetLineColor(3)
hRecInMass.SetFillColor(3)
hRecInMass.SetFillStyle(3004)

hMassEff.SetLineColor(2)
hMassEff78.SetLineColor(9)
hMassEff10.SetLineColor(3)
hMassEff1078.SetLineColor(6)
hMassEff15.SetLineColor(1)
hMassEff1578.SetLineColor(7)
hMassEff20.SetLineColor(4)
hMassEff2078.SetLineColor(5)

hRecMassEff.SetLineColor(2)
#hRecMassEff.SetFillColor(2)
#hRecMassEff.SetFillStyle(3004)

hRecMassEff78.SetLineColor(3)
#hRecMassEff78.SetFillColor(3)
#hRecMassEff78.SetFillStyle(3004)

hEtaLead.SetLineColor(3)
hEtaLead.SetFillColor(3)
hEtaLead.SetFillStyle(3004)

hEtaSub.SetLineColor(9)
#hEtaSub.SetFillColor(9)
#hEtaSub.SetFillStyle(3004)

hDeltaEta.SetLineColor(2)
hDeltaEta.SetFillColor(2)
hDeltaEta.SetFillStyle(3004)

hEtaEff.SetLineColor(9)
hEtaEff.SetFillColor(9)
hEtaEff.SetFillStyle(3004)

#draw histograms on the canvas and save this 
c1.cd(1)
hHLTwMU4.Draw()
print( "the total number of 4GeV muon entries =", hHLTwMU4.GetEntries())
print( "number of 4GeV muons not passing =", hHLTwMU4.GetBinContent(1))
print( "number of 4GeV muons passing =", hHLTwMU4.GetBinContent(2))
print( "overflow 4GeV muons =", hHLTwMU4.GetBinContent(3)) 
print( "passing + non passing 4GeV=", (hHLTwMU4.GetBinContent(1)+hHLTwMU4.GetBinContent(2)))
print( "trigger efficiency =", (hHLTwMU4.GetBinContent(2))/(hHLTwMU4.GetEntries()))

c1.cd(2)
hL1wMU6.Draw()
print( "the total number of 6GeV muon entries =", hL1wMU6.GetEntries())
print( "number of 6GeV muons not passing =", hL1wMU6.GetBinContent(1))
print( "number of 6GeV muons passing =", hL1wMU6.GetBinContent(2))
print( "overflow 6GeV muons =", hL1wMU6.GetBinContent(3)) 
print( "passing + non passing 6GeV=", (hL1wMU6.GetBinContent(1)+hL1wMU6.GetBinContent(2)))
print( "trigger efficiency =", (hL1wMU6.GetBinContent(2))/(hL1wMU6.GetEntries()))

#draw muon canvas plots
c2.cd(1)
hL1MuPt.Draw()
c2.cd(2)
hL1Mups.Draw()
c2.cd(3)
hHLTMups.Draw()

#draw Mlen plots
c3.cd(1)
hL1MuLen.Draw()
c3.cd(2)
hHLTMuLen.Draw()
c3.cd(3)
hL1MuPt.Draw()

#draw reco plots
c4.cd(1)
hRecMulen.Draw()
c4.cd(2)
hRecMups.Draw()
c4.cd(3)
hRecMuDR.Draw()
c4.cd(4)
hRecHLTMuDRFailMu6.Draw()

#draw L1 efficiency plots
c5.cd(1)
hL1Eff.Draw()
c5.cd(2)
hL1Mupass.Draw()
c5.cd(3)
hL1MuPt.Draw()

#draw reconstructed efficiency plots
c6.cd(1)
hRecL1Mupass.Draw()
c6.cd(2)
hRecMups.Draw()
c6.cd(3)
hRecL1Eff.Draw()

#draw delta phi plots
c7.cd(1)
hL1MuPhi.Draw()
c7.cd(2)
hHLMuPhi.Draw()
c7.cd(3)
hRecHLMuPhi.Draw()
c7.cd(4)
hRecL1MuPhi.Draw()

#Inv. Mass plots
c8.cd(1)
hInMass.Draw()
c8.cd(2)
hRecInMass.Draw()
c8.cd(3)
hMassEff.Draw()
hMassEff78.Draw("same")
c8.cd(4)
hRecMassEff.Draw()
hRecMassEff78.Draw("same")

#L1 plots
c9.cd(1)
hMuEta.Draw()
c9.cd(2)
hMuPhi.Draw()
c9.cd(3)
hMuDR.Draw()
c9.cd(4)
hL1MuPt.Draw()

#rec plots
c10.cd(1)
hRecMuEta.Draw()
c10.cd(2)
hRecMuPhi.Draw()
c10.cd(3)
hRecMuDR.Draw()
c10.cd(4)
hRecMups.Draw()

#Eff10 plots
c11.cd(1)
hL1Mu10pass.Draw()
c11.cd(2)
hL1MuPt.Draw()
c11.cd(3)
hL1Eff10.Draw()

#Eff 15 plots
c12.cd(1)
hL1Mu15pass.Draw()
c12.cd(2)
hL1MuPt.Draw()
c12.cd(3)
hL1Eff15.Draw()

#rec eff 10 plots
c13.cd(1)
hRecL1Mu10pass.Draw()
c13.cd(2)
hRecMups.Draw()
c13.cd(3)
hRecL1Eff10.Draw()

#rec eff 14 plots
c14.cd(1)
hRecL1Mu14pass.Draw()
c14.cd(2)
hRecMups.Draw()
c14.cd(3)
hRecL1Eff14.Draw()

#Mass eff plots
c15.cd(1)
hMassEff.Draw()
hMassEff78.Draw("same")
c15.cd(2)
hMassEff10.Draw()
hMassEff1078.Draw("same")
c15.cd(3)
hMassEff15.Draw()
hMassEff1578.Draw("same")
c15.cd(4)
hMassEff20.Draw()
hMassEff20.Draw("same")

#rec mass eff plots
c16.cd(1)
hRecMassEff.Draw()
hRecMassEff78.Draw("same")
c16.cd(2)
hRecMassEff10.Draw()
hRecMassEff1078.Draw("same")
c16.cd(3)
hRecMassEff14.Draw()
hRecMassEff1478.Draw("same")
c16.cd(4)
hRecMassEff20.Draw()
hRecMassEff20.Draw("same")

#mass eff dimuon plots
c17.cd(1)
hMassEff2Mu6.Draw()
hMassEff2Mu678.Draw("same")
c17.cd(2)
hMassEff2Mu10.Draw()
hMassEff2Mu1078.Draw("same")
c17.cd(3)
hMassEff2Mu20.Draw()
hMassEff2Mu2078.Draw("same")

#rec mass eff plots
c18.cd(1)
hRecMassEff2Mu6.Draw()
hRecMassEff2Mu678.Draw("same")
c18.cd(2)
hRecMassEff2Mu10.Draw()
hRecMassEff2Mu1078.Draw("same")
c18.cd(3)
hRecMassEff2Mu14.Draw()
hRecMassEff2Mu1478.Draw("same")

#eta plots
c19.cd(1)
hEtaLead.Draw()
hEtaSub.Draw("same")
c19.cd(2)
hDeltaEta.Draw()
c19.cd(3)
hEtaEff.Draw()

c1.SaveAs("canvasH.pdf")
c1.SaveAs("canvasH.gif")

c2.SaveAs("canvasMuon.gif")
c2.SaveAs("canvasMuon.pdf")

c3.SaveAs("canvasMLen.gif")
c3.SaveAs("canvasMLen.pdf")

c4.SaveAs("canvasreco.gif")
c4.SaveAs("canvasreco.pdf")

c5.SaveAs("canvasEff.gif")
c5.SaveAs("canvasEff.pdf")

c6.SaveAs("canvasRecEff.gif")
c6.SaveAs("canvasRecEff.pdf")

c7.SaveAs("canvasPhi.gif")
c7.SaveAs("canvasPhi.pdf")

c8.SaveAs("canvasMass.gif")
c8.SaveAs("canvasMass.pdf")

c9.SaveAs("canvasL1.gif")
c9.SaveAs("canvasL1.pdf")

c10.SaveAs("canvasRec.gif")
c10.SaveAs("canvasRec.pdf")

c11.SaveAs("canvasEff10.gif")
c11.SaveAs("canvasEff10.pdf")

c12.SaveAs("canvasEff15.gif")
c12.SaveAs("canvasEff15.pdf")

c13.SaveAs("canvasRecEff10.gif")
c13.SaveAs("canvasRecEff10.pdf")

c14.SaveAs("canvasRecEff15.gif")
c14.SaveAs("canvasRecEff15.pdf")

c15.SaveAs("canvasMassEff.gif")
c15.SaveAs("canvasMassEff.pdf")

c16.SaveAs("canvasRecMassEff.gif")
c16.SaveAs("canvasRecMassEff.pdf")

c17.SaveAs("canvas2MuEff.gif")
c17.SaveAs("canvas2MuEff.pdf")

c18.SaveAs("canvasRec2MuEff.gif")
c18.SaveAs("canvasRec2MuEff.pdf")

c19.SaveAs("canvasEta.gif")
c19.SaveAs("canvasEta.pdf")

outHistFile = ROOT . TFile . Open ("TraceyPlots.root","RECREATE")
outHistFile . cd ()

#write histograms to the file
#hHLTwMU24.Write()
#hHLTwMU26.Write()
#hHLTwMU60.Write()
#hHLTwMU40.Write()
hL1MuPt.Write()
hL1Mups.Write()
hHLTMups.Write()
hL1MuLen.Write()
hHLTMuLen.Write()
hMuNum.Write()
hL1Eff.Write()
hL1MuPt.Write()
hL1Mupass.Write()
hRecMulen.Write()
hRecMups.Write()
hRecMuDR.Write()
hRecHLTMuDRFailMu6.Write()
hRecL1Mupass.Write()
hRecMups.Write()
hRecL1Eff.Write()
hL1MuPhi.Write()
hHLMuPhi.Write()
hRecHLMuPhi.Write()
hRecL1MuPhi.Write()
hInMass.Write()
hRecInMass.Write()
hMuEta.Write()
hMuPhi.Write()
hMuDR.Write()
hRecMuEta.Write()
hRecMuPhi.Write()
hRecMuDR.Write()
hRecMups.Write()
hL1Mu10pass.Write()
hL1Eff10.Write()
hL1Mu15pass.Write()
hL1Eff15.Write()
hRecL1Mu10pass.Write()
hRecL1Eff10.Write()
hRecL1Mu14pass.Write()
hRecL1Eff14.Write()
hRecMassEff.Write()
hMassEff.Write()
hL1Eff2Mu6.Write() 
hL1Eff2Mu10.Write() 
hEtaLead.Write()
hEtaSub.Write()
hDeltaEta.Write()
hEtaLen.Write()
hEtaEff.Write()

outHistFile . Close ()
    


#reco_matched_dimu_mass = ROOT.TH1D("reco_matched_dimu_mass_2MU4")


print ("I made it to the end ")
