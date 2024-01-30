for i in 15 20 25 30 35 40 45 50 55 60
do
    cmsDriver.py "Configuration/Generator/python/fragment${i}.py" --python_filename "H4g-RunIIISummer22_NANOGEN_${i}GeV_cfg.py" --eventcontent NANOAODGEN --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAOD --fileout "file:nanoGen${i}.root" --conditions 124X_mcRun3_2022_realistic_postEE_v1 --step LHE,GEN,NANOGEN --era Run3 --no_exec --mc -n 10000

    printf "\n\n"
    sleep 2
done
