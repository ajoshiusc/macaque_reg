import os
import nibabel as nib
import nilearn as nil
import subprocess
import numpy as np
import glob

subid = "sub-1001"


sublist = glob.glob(
    "/deneb_disk/macaque_atlas_data/site-uwmadison_part1/sub-*/anat/*T1w.bse.nii.gz"
)


for t1 in sublist:
    subid = t1.split("/")[4]
    t1r = t1.replace('T1w.bse', 'T1w_1mm')

    outdir = '/deneb_disk/macaque_atlas_data/out_animal_warper/' + subid
    
    cmd = f'3dresample -input {t1} -prefix {t1r} -dxyz 1 1 1'
    os.system(cmd)


    cmd = f'@animal_warper -echo -input {t1r} -input_abbrev {subid} -base /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/NMT_v2.1_sym_05mm_SS.nii.gz -base_abbrev NMT2 -atlas_followers /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/CHARM_in_NMT_v2.1_sym_05mm.nii.gz /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/D99_atlas_in_NMT_v2.1_sym_05mm.nii.gz -atlas_abbrevs CHARM D99 -seg_followers /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/NMT_v2.1_sym_05mm_segmentation.nii.gz -seg_abbrevs SEG -outdir {outdir} -ok_to_exist'
    os.system(cmd)
    print(cmd)
    

