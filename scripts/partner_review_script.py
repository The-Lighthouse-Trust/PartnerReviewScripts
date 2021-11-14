import pandas as pd
import numpy as np
import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))

partner_review_file = dir_path+'\\Partner_Review_File.xlsx' # PEPFAR Partner preview file.
tx_pvls = pd.read_excel(partner_review_file, sheet_name=0, skiprows=1, usecols=['SiteName', 'orgUnit', 'PrimePartner',
       'attributeOptionCombo', 'FundingAgency', 'EMRSiteType', 'SupportType','TX_PVLS (D) Total.1',
       'TX_PVLS (N) Total.1'])
tx_pvls.columns = ['SiteName', 'orgUnit', 'PrimePartner','attributeOptionCombo', 'FundingAgency', 'EMRSiteType', 'SupportType',
        'TX_PVLS (D)', 'TX_PVLS (N)']
tx_pvls = tx_pvls[tx_pvls['PrimePartner'] == 'Lighthouse']

hts = pd.read_excel(partner_review_file, sheet_name=1, skiprows=1, usecols=['SiteName', 'orgUnit', 'PrimePartner',
       'attributeOptionCombo', 'FundingAgency', 'EMRSiteType', 'SupportType','IP Manually Entered Result- HTS_TST.1',
       'IP Manually Entered Result-  HTS_POS.1','IP Manually Entered Result- HTS_SELF.1'])
hts.columns = ['SiteName', 'orgUnit', 'PrimePartner','attributeOptionCombo', 'FundingAgency', 'EMRSiteType', 'SupportType','HTS_TST',
       'HTS_POS','HTS_SELF']
hts = hts[hts['PrimePartner'] == 'Lighthouse']

pmtct = pd.read_excel(partner_review_file, sheet_name=2, skiprows=1, usecols=['SiteName', 'orgUnit', 'PrimePartner',
       'attributeOptionCombo', 'FundingAgency', 'EMRSiteType', 'SupportType',
       'IP Manually Entered Result- PMTCT_STAT (D).1',
       'IP Manually Entered Result- PMTCT_STAT (N).1',
       'PMTCT_ART.1', 'PMTCT_EID.1'])
pmtct.columns = ['SiteName', 'orgUnit', 'PrimePartner',
       'attributeOptionCombo', 'FundingAgency', 'EMRSiteType', 'SupportType',
       'PMTCT_STAT (D)','PMTCT_STAT (N)','PMTCT_ART', 'PMTCT_EID']
pmtct = pmtct[pmtct['PrimePartner'] == 'Lighthouse']

hts_index = pd.read_excel(partner_review_file, sheet_name=3)
tb = pd.read_excel(partner_review_file, sheet_name =4)
vmmc = pd.read_excel(partner_review_file, sheet_name=5)

mergeddf = hts.merge(pmtct, on=['SiteName', 'orgUnit']).merge(tx_pvls, on=['SiteName', 'orgUnit'])

print(mergeddf.columns)

lh_indicator_file = dir_path+'\\LH_Indicator_File.xlsx'
lh_data = pd.DataFrame()
lh_data = lh_data.append(pd.read_excel(lh_indicator_file))

indicators = lh_data.columns


# Review HTS report
# Clean headers
# hts.columns = [''] * len(hts.columns)
# hts.columns = hts.iloc[0].values
# hts = hts[1:]
# hts = hts[hts['PrimePartner'] == 'Lighthouse'] # Lighthouse data only
# hts = hts.sort_values('orgUnit')
# hts = hts.reset_index(drop=True, inplace=True)

# lh_data = lh_data.sort_values('orgUnit')
# lh_data = lh_data.reset_index(drop=True, inplace=True)

# hts['HTS_TST'] = lh_data['HTS_TST']
# # Compare the values and create a column for results
# hts['HTS_TST_COMPARE_BOOL'] = hts['IP Manually Entered Result- HTS_TST'] == hts['HTS_TST']

# def compare_with_lh(pepfar_data, pepfar_indicator, lh_data, lh_indicator):
#     pepfar_data[lh_indicator] = lh_data[lh_indicator]
#     pepfar_data[lh_indicator + '_COMPARE_BOOL'] = pepfar_data[pepfar_indicator] == pepfar_data[lh_indicator]
#     pepfar_data[lh_indicator + '_COMPARE_VAL'] = pepfar_data[pepfar_indicator] - pepfar_indicator[lh_indicator]
#     return pepfar_data

# def compare_with_dha(pepfar_data, ip_indicator, dha_indicator):
#     pepfar_data[ip_indicator + '_COMPARE_BOOL'] = pepfar_data[dha_indicator] == pepfar_data[ip_indicator]
#     pepfar_data[ip_indicator + '_COMPARE_VAL'] = pepfar_data[dha_indicator] - pepfar_data[ip_indicator]
#     return pepfar_data