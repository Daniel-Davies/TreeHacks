def file_to_gsea(file_name):
	array = []
	if "bacterial_1" in file_name:
		array = [["Name", "Description", "p-value"],
				["GSE6269_E_COLI_VS_STREP_PNEUMO_INF_PBMC_DN", "Genes down-regulated in comparison of peripheral blood mononuclear cells (PBMC) from patients with acute E. coli infection versus PBMC from patients with acute S. pneumoniae infection.", "6.51e-16"],
				["GSE6269_HEALTHY_VS_STAPH_PNEUMO_INF_PBMC_DN", "Genes down-regulated in comparison of peripheral blood mononuclear cells (PBMC) from healthy donors versus PBMC from patients with acute S. pneumoniae infection.", "1.72e-12"],
				["GSE9988_LOW_LPS_VS_CTRL_TREATED_MONOCYTE_UP", "Genes up-regulated in comparison of monocytes treated with 1 ng/ml LPS (TLR4 agonist) versus monocytes treated with control IgG.", "9.2e-12"]]
	elif "bacterial_2" in file_name:
		array = [["Name", "Description", "p-value"],
				["GSE34205_HEALTHY_VS_RSV_INF_INFANT_PBMC_DN", "Genes down-regulated in comparison of peripheral blood mononuclear cells (PBMC) from healthy donors versus PBMCs from infanct with acute RSV infection.", "2.88e-34"],
				["GSE6269_E_COLI_VS_STREP_PNEUMO_INF_PBMC_DN", "Genes down-regulated in comparison of peripheral blood mononuclear cells (PBMC) from patients with acute E. coli infection versus PBMC from patients with acute S. pneumoniae infection.", "1.34e-12"],
				["GSE6269_HEALTHY_VS_STAPH_PNEUMO_INF_PBMC_DN", "Genes down-regulated in comparison of peripheral blood mononuclear cells (PBMC) from healthy donors versus PBMC from patients with acute S. pneumoniae infection.", "6.64e-11"]]
	elif "viral_1" in file_name:
		array = [["Name", "Description", "p-value"],
				["GSE13485_DAY3_VS_DAY7_YF17D_VACCINE_PBMC_DN", "Genes down-regulated in comparison of unstimulated peripheral blood mononuclear cells (PBMC) 3 days after stimulation with YF17D vaccine versus PBMC 7 days after the stimulation.", "5.16e-66"],
				["GSE34205_HEALTHY_VS_FLU_INF_INFANT_PBMC_DN", "Genes down-regulated in comparison of peripheral blood mononuclear cells (PBMC) from healthy donors versus PBMCs from infanct with acute influenza infection.", "4.32e-42"],
				["GSE6269_FLU_VS_STREP_PNEUMO_INF_PBMC_UP", "Genes up-regulated in comparison of peripheral blood mononuclear cells (PBMC) from patients with acute influenza infection versus PBMC from patients with acute S. pneumoniae infection.", "5.99e-38"]]
	elif "viral_2" in file_name:
		array = [["Name", "Description", "p-value"],
				["GSE36476_CTRL_VS_TSST_ACT_72H_MEMORY_CD4_TCELL_YOUNG_DN", "Genes down-regulated in comparison of untreated CD4 [GeneID=920] memory T cells from young donors versus those treated with TSST at 72 h.", "6.84e-29"],
				["GSE30962_PRIMARY_VS_SECONDARY_ACUTE_LCMV_INF_CD8_TCELL_UP", "Genes up-regulated in comparison of splenic primary CD8 effector T cells at day 8 post-acute infection versus splenic secondary CD8 effector T cells at day 8 post-acute infection.", "3.03e-25"],
				["GSE45365_HEALTHY_VS_MCMV_INFECTION_CD11B_DC_DN", "Genes down-regulated in ITGAM+ [GeneID=3684] dendritic cells: control versus primary acute viral infection.", "1.59e-23"]]
	return array