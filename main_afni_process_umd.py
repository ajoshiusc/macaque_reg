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
    



    outdir = '/deneb_disk/macaque_atlas_data/out_animal_fmri'
    # cmd = f'@animal_warper -echo -input {t1r} -input_abbrev {subid} -base /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/NMT_v2.1_sym_05mm_SS.nii.gz -base_abbrev NMT2 -atlas_followers /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/CHARM_in_NMT_v2.1_sym_05mm.nii.gz /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/D99_atlas_in_NMT_v2.1_sym_05mm.nii.gz -atlas_abbrevs CHARM D99 -seg_followers /home/ajoshi/MACAQUE_DEMO/NMT_v2.1_sym/NMT_v2.1_sym_05mm/NMT_v2.1_sym_05mm_segmentation.nii.gz -seg_abbrevs SEG -outdir {outdir} -ok_to_exist'
    
    cmd = f'cd {outdir}; afni_proc.py                                                                \
    -subj_id                  {subid}                                       \
    -blocks            tshift align tlrc volreg blur mask scale regress     \
    -dsets                    /deneb_disk/macaque_atlas_data/site-uwmadison_part1/{subid}/func/{subid}_task-rest_bold.nii.gz                                  \
    -copy_anat                /deneb_disk/macaque_atlas_data/out_animal_warper/{subid}/{subid}_nsu.nii.gz                                    \
    -anat_has_skull           no                                            \
    -anat_uniform_method      none                                          \
    -radial_correlate_blocks  tcat volreg                                   \
    -radial_correlate_opts    -sphere_rad 14                                \
    -tcat_remove_first_trs    2                                      \
    -volreg_align_to          MIN_OUTLIER                                   \
    -volreg_align_e2a                                                       \
    -volreg_tlrc_warp                                                       \
    -volreg_warp_dxyz         1.25                                 \
    -volreg_compute_tsnr      yes                                           \
    -align_opts_aea           -cost "lpc+ZZ" -giant_move               \
                              -cmass cmass -feature_size 0.5    \
    -align_unifize_epi        yes                                \
    -tlrc_base                /home/ajoshi/MACAQUE_DEMO_REST/NMT_v2.1_sym/NMT_v2.1_sym_05mm/NMT_v2.1_sym_05mm_SS.nii.gz                                   \
    -tlrc_NL_warp                                                           \
    -tlrc_NL_warped_dsets     /deneb_disk/macaque_atlas_data/out_animal_warper/{subid}/{subid}_warp2std_nsu.nii.gz /deneb_disk/macaque_atlas_data/out_animal_warper/{subid}/{subid}_composite_linear_to_template.1D /deneb_disk/macaque_atlas_data/out_animal_warper/{subid}/{subid}_shft_WARP.nii.gz                              \
    -blur_size                2.0                                  \
    -regress_motion_per_run                                                 \
    -regress_apply_mot_types  demean deriv                                  \
    -regress_censor_motion    0.1                                 \
    -regress_censor_outliers  0.02                               \
    -regress_est_blur_errts                                                 \
    -regress_est_blur_epits                                                 \
    -regress_run_clustsim     no                                            \
    -html_review_style        pythonic; tcsh -xef proc.{subid} 2>&1 | tee output.proc.{subid}' 

    os.system(cmd)

    print(cmd)

    #os.system(f'tcsh -xef proc.sub-1005 2>&1 | tee output.proc.sub-1005')
