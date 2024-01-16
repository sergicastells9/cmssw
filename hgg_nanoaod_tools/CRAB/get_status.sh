for VAR in 15 20 25 30 35 40 45 50 55 60
do
    crab status --long --verboseErrors "MNConversion_crab/crab_MNConversion_HAHMHToAA_AToGG_MA_"$VAR"GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018/" > "MNConversion_crab/crab_MNConversion_HAHMHToAA_AToGG_MA_"$VAR"GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018/status_long_backup.txt"
    echo "Saved status for ${VAR} GeV jobs"
done

echo "All done."
