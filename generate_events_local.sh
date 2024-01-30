for i in 15 20 25 30 35 40 45 50 55 60
do
    if [ ! -f "nanoGen${i}.root" ]; then
        cmsRun "H4g-RunIIISummer22_NANOGEN_${i}GeV_cfg.py"
        printf "\n\n"
        sleep 2
    fi
done
