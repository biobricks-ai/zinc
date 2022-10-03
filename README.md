# Zinc 20

> ZINC20 (https://zinc20.docking.org/) is a free database of commercially-available compounds for virtual screening. ZINC contains over 230 million purchasable compounds in ready-to-dock, 3D formats. ZINC also contains over 750 million purchasable compounds you can search for analogs in under a minute.


1. Create a brick named `{newbrick}` from this template
```
gh repo create biobricks-ai/{newbrick} -p biobricks-ai/brick-template --public
gh repo clone biobricks-ai/{newbrick}
cd newbrick
```

2. Replace stages/1_stage.sh with your own stages
    Recommended scripts:
    - ``0_download.sh``
    - ``1_unzip.sh``
    - ``2_build.sh`` calling a function to process individual files like ``originalformat2parquet.R`` or ``originalformat2parquet.py``

3. Replace stages in dvc.yaml with your new stages
    
4. Build your brick
```
dvc repro # runs new stages
```
5. Push the data to biobricks.ai
```
dvc push -r s3.biobricks.ai 
```
6. commit the brick
```
git add -A && git commit -m "some message"
git push
```
7. monitor the bricktools github action

