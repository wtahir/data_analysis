def pr_cr_er(cer_0, cerGreater_0_lessThan_threshold, cer_greaterThreshold, detected_files, total_files):
    
    pr = cer_0/total_files
    dr = detected_files/ total_files
    cr = cerGreater_0_lessThan_threshold/ total_files
    er = cer_greaterThreshold/ total_files
    print ("PR = '{}, 'CR = ' {}, ER = {}, DR = {}".format(pr, cr, er, dr))
