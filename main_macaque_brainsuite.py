#||AUM||
#||Shree Ganeshaya Namaha||

import os

#t1 = '/deneb_disk/macaque_atlas_data/sub-032186/ses-001/anat/sub-032186_ses-001_acq-mp2rage_run-1_T1w.nii.gz'
t2='/deneb_disk/macaque_atlas_data/sub-032186/ses-001/anat/sub-032186_ses-001_run-1_T2w.nii.gz'
subid = 'sub-032186_t2'





outdir,fname = os.path.split(t2)


cmd = f'@animal_warper -echo -input {t2} -input_abbrev {subid} -base /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/NMT_v2.1_sym_05mm_SS.nii.gz -base_abbrev NMT2 -atlas_followers /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/CHARM_in_NMT_v2.1_sym_05mm.nii.gz /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/D99_atlas_in_NMT_v2.1_sym_05mm.nii.gz -atlas_abbrevs CHARM D99 -seg_followers /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/NMT_v2.1_sym_05mm_segmentation.nii.gz -seg_abbrevs SEG -skullstrip /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/NMT_v2.1_sym_05mm_brainmask.nii.gz -outdir {outdir} -ok_to_exist'


os.system(cmd)
