import pandas as pd
import yfinance as yf
import datetime
from statistics import mean
#from tqdm import tqdm
#import threading
import time

list_ticks = ['TACO', 'CPIX', 'BCEL', 'PLIN', 'BHAT', 'GTYH', 'ENOB', 'MESO', 'NM', 'QNST', 'GOL', 'SYRS', 'CDLX', 'CANG', 'FRGI', 'NCLH', 'TRIP', 'LCI', 'ATHM', 'ODT', 'HUYA', 'HA', 'TWI', 'TR', 'NKTR', 'RAIL', 'AZUL', 'TAST', 'IIIV', 'BABA', 'CCL', 'SKYW', 'PBTS', 'RCL', 'CNK', 'PLAY', 'PRTY', 'SABR', 'UAL', 'TDS', 'FLNT', 'CUK', 'QUOT', 'CVET', 'AAL', 'LIND', 'HTZ', 'HMLP', 'BZUN', 'VIOT', 'PFGC', 'APRN', 'EVRI', 'PK', 'ATRO', 'EPZM', 'EB', 'MORF', 'BNED', 'BJRI', 'SWAV', 'DESP', 'CODI', 'NVRO', 'FARM', 'SGMS', 'JG', 'SCPL', 'SHAK', 'LVS', 'LOCO', 'MMYT', 'NUVA', 'SAM', 'VFF', 'SNOA', 'MHO', 'CYCN', 'NINE', 'TISI', 'MLCO', 'SEED', 'SAVE', 'EXPE', 'LILA', 'YY', 'DAL', 'ACIW', 'LYV', 'BEST', 'BIDU', 'REKR', 'EGHT', 'SIBN', 'WYNN', 'RRGB', 'KNOP', 'HXL', 'USFD', 'CORT', 'MDC', 'MRKR', 'KBR', 'HIBB', 'PI', 'BV', 'SNBR', 'NTUS', 'RWLK', 'ARTL', 'TGI', 'UBER', 'LYFT', 'USM', 'POLA', 'EEFT', 'ASLN', 'INSW', 'ESPR', 'REPH', 'OPTN', 'PENN', 'VYGR', 'CHEF', 'ALGT', 'IQ', 'SIEN', 'XPER', 'KNDI', 'GMED', 'ELOX', 'HRI', 'RL', 'OLLI', 'PAR', 'PINS', 'PCG', 'AMED', 'SY', 'CPA', 'GPN', 'KSS', 'SSTK', 'DIN', 'BLMN', 'CTSO', 'PVH', 'AXNX', 'BKNG', 'TWTR', 'RYTM', 'LHCG', 'MRIN', 'VCEL', 'TPIC', 'ALNA', 'MGM', 'USWS', 'AGS', 'SPR', 'PRPL', 'SCSC', 'QTWO', 'MAXR', 'RMBL', 'ATEC', 'IPDN', 'INST', 'H', 'ERJ', 'BYSI', 'EXAS', 'CCS', 'HBI', 'TXRH', 'VEEV', 'RUTH', 'IGT', 'CBRL', 'HEXO', 'CAKE', 'RH', 'BZH', 'BXC', 'BRFS', 'JBLU', 'TFX', 'RMED', 'TPH', 'BJ', 'PSNL', 'RYI', 'DOCU', 'RDNT', 'AAN', 'NEW', 'PRMW', 'SEAS', 'XBIO', 'TG', 'NMM', 'EBIX', 'CUTR', 'VAC', 'TTOO', 'CVM', 'PLNT', 'PLAN', 'FTDR', 'VRA', 'AXL', 'OUT', 'NCMI', 'QD', 'JFIN', 'FLR', 'STNG', 'ELY', 'GES', 'KBH', 'TRUE', 'ASC', 'RCII', 'AL', 'PRTK', 'MAR', 'MESA', 'SBLK', 'ALK', 'BBBY', 'TRVG', 'MATX', 'SWX', 'ATGE', 'CNHI', 'EVH', 'BYND', 'MELI', 'CBIO', 'HUBG', 'TRN', 'PRIM', 'ARMK', 'RDFN', 'GLPG', 'SGRY', 'ZIOP', 'FAMI', 'SAH', 'HELE', 'ZGNX', 'ABG', 'GPS', 'KFY', 'CNMD', 'ITGR', 'VLRS', 'SUM', 'ANGI', 'COTY', 'PLYA', 'HQY', 'AWI', 'PEN', 'LPCN', 'FICO', 'JMIA', 'SYY', 'CHGG', 'FWRD', 'TIGR', 'OGS', 'EVTC', 'SRPT', 'CPRI', 'FSLY', 'ZBH', 'KNX', 'TPX', 'SWM', 'ATRC', 'CARG', 'FGEN', 'OLED', 'LOPE', 'PTCT', 'FLT', 'SBH', 'AEO', 'DENN', 'ITRI', 'TMHC', 'HLT', 'URI', 'ORGS', 'VSAT', 'ITT', 'WEX', 'ANDE', 'SEM', 'BFAM', 'BLDR', 'BLKB', 'ACA', 'IBP', 'GBX', 'YUMC', 'TPR', 'UHS', 'MITO', 'TSEM', 'ANF', 'GFF', 'CHUY', 'SILK', 'DPW', 'SHEN', 'AVYA', 'GMS', 'STIM', 'TCDA', 'VRRM', 'BW', 'ITRM', 'CRS', 'ORGO', 'CTRN', 'ONTX', 'HEES', 'INSM', 'OSIS', 'CI', 'CP', 'SHOO', 'MTN', 'ARLO', 'HGV', 'GLDD', 'SUNW', 'MD', 'NRG', 'IHG', 'SIX', 'SKY', 'TDG', 'THS', 'FB', 'BBW', 'LZB', 'AVNS', 'CAMP', 'GNK', 'NBEV', 'HI', 'TV', 'UIS', 'TGTX', 'FIS', 'GE', 'AIR', 'YELP', 'CRH', 'BECN', 'IONS', 'EHC', 'DBD', 'WH', 'IMAX', 'BSX', 'CARS', 'COLM', 'CETX', 'EW', 'RAD', 'KR', 'ENS', 'TILE', 'MMSI', 'FRO', 'FNKO', 'WING', 'TOL', 'CRON', 'SFIX', 'TSE', 'AERI', 'AUTL', 'INTC', 'KMT', 'PHM', 'CRUS', 'EXPO', 'KNSA', 'JNCE', 'ABM', 'BCO', 'SCS', 'LII', 'COLL', 'PGTI', 'ZUMZ', 'TCMD', 'DHT', 'CCOI', 'CHS', 'WBA', 'OSMT', 'REZI', 'SYK', 'BNFT', 'RGNX', 'BUD', 'FMS', 'PRO', 'VMC', 'GOGL', 'NCR', 'VSTO', 'GT', 'SR', 'ACM', 'CSII', 'SFL', 'ENSG', 'AER', 'CDZI', 'PRGO', 'SLDB', 'RRR', 'SSD', 'RADA', 'NEO', 'TGH', 'DCI', 'HAE', 'MGA', 'NWL', 'DVA', 'AGCO', 'ICPT', 'TNET', 'GO', 'WEN', 'SATS', 'BKD', 'GBT', 'RARE', 'RDHL', 'BA', 'EPC', 'MUSA', 'NDLS', 'CEPU', 'DISH', 'PTC', 'HRB', 'MTZ', 'NTES', 'WKHS', 'BYD', 'MERC', 'MYOV', 'RAMP', 'CR', 'BLD', 'FLS', 'PAYS', 'YUM', 'GKOS', 'TTGT', 'CAE', 'DRI', 'ENV', 'AMGN', 'PACK', 'EAT', 'WIX', 'XPO', 'FISV', 'NJR', 'MAN', 'LAUR', 'MCS', 'IIVI', 'SNDX', 'OI', 'MDT', 'MOD', 'GRIN', 'NWN', 'CALA', 'HOG', 'DOYU', 'BCOR', 'BLDP', 'ADS', 'ARCE', 'ULTA', 'CYRX', 'ENLV', 'ACAD', 'LOVE', 'BHC', 'BKE', 'CNP', 'LUV', 'SEE', 'ALGN', 'PSTV', 'DHI', 'ACLS', 'CASY', 'CONN', 'ACOR', 'QTRX', 'AMCX', 'EVOP', 'QURE', 'SIG', 'REAL', 'TWNK', 'CAR', 'INGR', 'INSP', 'ABMD', 'GIII', 'LEG', 'SJI', 'AVY', 'OSTK', 'GTN', 'TJX', 'ALSN', 'PLCE', 'R', 'IRWD', 'RESN', 'ABEO', 'AVLR', 'GEF', 'TEX', 'FORM', 'PCRX', 'ATI', 'GPRO', 'CHKP', 'IART', 'MMM', 'BWXT', 'PTNR', 'ACB', 'SO', 'HVT', 'IEX', 'RNG', 'BAND', 'FAST', 'GCI', 'MAT', 'MYGN', 'TKR', 'HYRE', 'UPLD', 'UGI', 'VIAV', 'IAA', 'AEIS', 'XRX', 'TRTN', 'KSU', 'UAA', 'JELD', 'PBI', 'JKHY', 'SNAP', 'OCX', 'GLYC', 'GOLF', 'HRTX', 'MBIO', 'STAA', 'TLYS', 'WK', 'CNSL', 'PRAA', 'FSS', 'FUN', 'PCH', 'INSG', 'NVGS', 'HUM', 'SNN', 'CTSH', 'ROST', 'SLGG', 'VCYT', 'CRTO', 'POST', 'GSL', 'B', 'HII', 'TAP', 'MTOR', 'ZYNE', 'TTC', 'PRLB', 'TLRY', 'KEX', 'LSTR', 'AUPH', 'GTLS', 'BC', 'DDD', 'WCC', 'IPGP', 'MOGU', 'TMUS', 'ADT', 'HLF', 'DMTK', 'MITK', 'DAN', 'DLX', 'RFP', 'ACCO', 'CYTK', 'CSX', 'OGI', 'STRA', 'CW', 'TS', 'UA', 'MCD', 'SWI', 'TBI', 'IOVA', 'PSN', 'ALNY', 'DAKT', 'CFX', 'EOLS', 'HCAT', 'JBT', 'TUP', 'MIDD', 'NLTX', 'PZZA', 'QSR', 'EVRG', 'THO', 'WHR', 'NTGR', 'EVA', 'PHG', 'TPC', 'XYL', 'WRK', 'AMCR', 'MTLS', 'BWA', 'NTCT', 'RUBY', 'KO', 'JWN', 'AGTC', 'OMCL', 'UL', 'CSV', 'GVA', 'TXT', 'DIS', 'MGPI', 'MNOV', 'AES', 'SMSI', 'PM', 'MNRO', 'BL', 'GGG', 'MHK', 'TECH', 'NSC', 'PDD', 'EDIT', 'JBHT', 'PCAR', 'HE', 'DAR', 'MLM', 'COUP', 'GALT', 'MNST', 'NEPT', 'STE', 'GWRE', 'INGN', 'SLRX', 'IDT', 'CCEP', 'NESR', 'CHH', 'SON', 'CELH', 'MOMO', 'NI', 'GLNG', 'ANTM', 'ARVN', 'MWA', 'WWW', 'ETON', 'ALE', 'DXC', 'HEI', 'TDY', 'CAPR', 'TEVA', 'AVA', 'LEA', 'OTEX', 'SBGI', 'RFL', 'AAPL', 'BILI', 'NVTA', 'ENR', 'NUS', 'RYN', 'SUZ', 'MGNX', 'NVCR', 'SAP', 'DEO', 'FTS', 'SOHU', 'G', 'VSH', 'ADNT', 'APTX', 'COO', 'LEN', 'IRDM', 'CL', 'WMS', 'SNDR', 'SWKS', 'CGC', 'MTH', 'EGLE', 'MRCY', 'BKH', 'WSC', 'ATSG', 'GOGO', 'NSTG', 'UFPI', 'UNH', 'ELAN', 'EXTR', 'FIVE', 'RLGT', 'PH', 'CTT', 'ETN', 'GDS', 'GIL', 'NVT', 'SAGE', 'SFM', 'TME', 'M', 'AAOI', 'KTOS', 'SWIR', 'GPC', 'DE', 'CSL', 'SANM', 'SBUX', 'TEN', 'EXPR', 'HTLD', 'MREO', 'OGE', 'EIX', 'CLVS', 'PPL', 'ALLE', 'CAT', 'FDX', 'TER', 'FOLD', 'GDDY', 'UNP', 'ADTN', 'CTAS', 'GOSS', 'OC', 'MCK', 'RMD', 'THC', 'ARCO', 'FVRR', 'PRQR', 'PKG', 'ADSK', 'EURN', 'GOOS', 'SCOR', 'SSNC', 'ST', 'CTS', 'EXP', 'ANSS', 'NXTC', 'ROAD', 'JNJ', 'WWD', 'CDK', 'DBI', 'OKE', 'SNX', 'CERN', 'EXEL', 'MANU', 'TCRR', 'CWT', 'ANGO', 'NEOG', 'OSUR', 'MSM', 'AMPH', 'ZG', 'ABBV', 'KHC', 'KMX', 'PIRS', 'SLGN', 'BEP', 'MDU', 'NWE', 'DG', 'ABB', 'LMT', 'STZ', 'GMRE', 'SNDL', 'VFC', 'QRVO', 'RDWR', 'URBN', 'CNR', 'DTE', 'VOD', 'AMRC', 'LITE', 'CMG', 'CRI', 'TDC', 'AGRO', 'AKBA', 'ATO', 'DOV', 'GTHX', 'SYNH', 'XRAY', 'SKX', 'CVS', 'MTCH', 'HD', 'LL', 'EVFM', 'GSKY', 'LEVI', 'PDCO', 'WAB', 'CNDT', 'NLSN', 'KTB', 'LPX', 'PTE', 'TLK', 'LDOS', 'SGMO', 'ABT', 'CLS', 'CLH', 'STM', 'CVLT', 'MRVL', 'EL', 'EME', 'KEP', 'ARNA', 'ASMB', 'COHU', 'KALV', 'PAYX', 'JAZZ', 'AZN', 'WGO', 'HSIC', 'HUBB', 'FIVN', 'FLEX', 'PTGX', 'LW', 'PD', 'UCTT', 'NOC', 'BMRN', 'CTXS', 'MDLZ', 'TENB', 'YMAB', 'BAX', 'MKC', 'SRE', 'WAT', 'DXCM', 'HCSG', 'RELX', 'CDW', 'OSK', 'SJM', 'AMKR', 'HTHT', 'SCVL', 'SYBX', 'UPWK', 'ETR', 'HON', 'BOOT', 'LAD', 'NDSN', 'CHD', 'EXC', 'HALO', 'MDRX', 'OBSV', 'ITW', 'ROKU', 'CAL', 'CNI', 'CYH', 'HCA', 'SWK', 'HOOK', 'ILMN', 'ALV', 'GWW', 'ADVM', 'LOGI', 'DY', 'AMBA', 'LECO', 'IAC', 'POR', 'AYI', 'MEI', 'CHDN', 'MIME', 'AVGO', 'MTW', 'NOVT', 'ORTX', 'COMM', 'ABC', 'APH', 'SSP', 'LNT', 'FLOW', 'TCS', 'BLIN', 'BLUE', 'CALM', 'GLW', 'D', 'IP', 'AEP', 'FOX', 'FUV', 'OMC', 'RBA', 'BBIO', 'FOXA', 'NTNX', 'EAF', 'PNR', 'APTV', 'DSKE', 'NFLX', 'AMAT', 'AAP', 'RGS', 'CVNA', 'NATI', 'TRHC', 'TU', 'ROL', 'ALEC', 'NXGN', 'ROP', 'AMZN', 'UTHR', 'WERN', 'HOLI', 'CMI', 'SRCL', 'EPAY', 'CCI', 'JBL', 'TEL', 'WW', 'AEE', 'CMS', 'BPMC', 'OPGN', 'TTEK', 'EBR', 'CGEN', 'ORCC', 'TDOC', 'VERI', 'AY', 'ACHC', 'SRTS', 'GPK', 'GSK', 'RCM', 'TWOU', 'A', 'ATR', 'IPG', 'TRU', 'BERY', 'INMD', 'CAG', 'CCK', 'AVRO', 'FLWS', 'LOMA', 'CRBP', 'NSIT', 'PAG', 'ALRM', 'MOSY', 'SBS', 'ZEN', 'DNLI', 'AOS', 'ARW', 'LHX', 'MU', 'CNC', 'DUK', 'RCI', 'SPB', 'ABIO', 'NGM', 'TSN', 'CHNG', 'SWCH', 'NGG', 'CPRX', 'LKCO', 'CCXI', 'SSYS', 'PG', 'BTI', 'CAH', 'ELF', 'MASI', 'DQ', 'AWK', 'PHAS', 'AXSM', 'CHRW', 'NBIX', 'EMR', 'WEC', 'CGNX', 'ADM', 'ALC', 'BDX', 'BB', 'EA', 'MO', 'ALKS', 'APPS', 'SYNA', 'CSCO', 'DOMO', 'ICHR', 'NOVA', 'VKTX', 'AVT', 'DVAX', 'MX', 'TM', 'LKQ', 'CACI', 'CNCE', 'GD', 'BIP', 'KDP', 'LRN', 'CTRM', 'LRCX', 'QTNT', 'TEAM', 'IBM', 'ADMA', 'MMS', 'ATVI', 'AXGN', 'CDXC', 'VOXX', 'XENE', 'TK', 'RPD', 'SGH', 'FIZZ', 'SIMO', 'TTMI', 'TWLO', 'ED', 'CCU', 'RVLV', 'UNFI', 'AVDL', 'VREX', 'AMC', 'PEP', 'INSE', 'AZO', 'Z', 'IMUX', 'NOMD', 'THRM', 'ES', 'BCE', 'NNBR', 'PDSB', 'IR', 'MSI', 'SMPL', 'IDXX', 'ADP', 'LOW', 'ALLT', 'FE', 'MSCI', 'TBPH', 'SRI', 'NEWT', 'WTRH', 'FULC', 'DLB', 'PWR', 'RUN', 'OCUL', 'PHUN', 'TGNA', 'RGR', 'SNY', 'ASND', 'CASA', 'VST', 'WMT', 'AMRX', 'ANIX', 'MSFT', 'PINC', 'SPOT', 'VRNS', 'AAON', 'TAK', 'EDSA', 'GOOG', 'PII', 'CSIQ', 'HMHC', 'AN', 'BR', 'NWS', 'LPG', 'LSCC', 'PEGA', 'BMY', 'ZM', 'AME', 'TGS', 'DLTR', 'K', 'HRL', 'COHR', 'DAC', 'ERII', 'AYX', 'DOX', 'IVC', 'IQV', 'NCNA', 'AJRD', 'AKRO', 'COST', 'SMAR', 'KN', 'ADBE', 'FSLR', 'STOK', 'NEE', 'IRBT', 'JCI', 'GLOB', 'BURL', 'EIGR', 'FBHS', 'AAWW', 'DFIN', 'HOLX', 'KPTI', 'NWSA', 'OKTA', 'VRSN', 'DTIL', 'MRUS', 'ORLY', 'JNPR', 'LQDT', 'WATT', 'WDAY', 'WWE', 'TTD', 'ENDP', 'ISRG', 'RCKT', 'NVS', 'F', 'SCI', 'SPH', 'RVI', 'CRVS', 'KURA', 'POOL', 'KMB', 'OMI', 'GNTX', 'STRO', 'PNM', 'PSTG', 'HAS', 'HSY', 'APM', 'JYNT', 'KLDO', 'VRTX', 'BAH', 'MLI', 'UPS', 'WCN', 'AQUA', 'NIU', 'TXN', 'WVE', 'XEL', 'DELL', 'INMB', 'LNTH', 'HMC', 'CDNA', 'SHOP', 'SMTC', 'PEG', 'PPC', 'EXPD', 'YEXT', 'GM', 'RACE', 'BG', 'ANET', 'IDRA', 'NVO', 'VGR', 'HARP', 'OMER', 'DCPH', 'ORCL', 'SAFM', 'ACN', 'SPI', 'PAYC', 'AMN', 'SJR', 'ATUS', 'FFIV', 'NOVN', 'MFGP', 'ASPN', 'YETI', 'GIS', 'IEA', 'LIVN', 'TRMD', 'SAIC', 'CIEN', 'CPB', 'BIIB', 'MTEM', 'BE', 'FTV', 'KOD', 'BOX', 'ATKR', 'DSGX', 'MKSI', 'FL', 'EBS', 'NOW', 'CYBR', 'SLAB', 'PNW', 'ENTX', 'INFO', 'WY', 'EVBG', 'AMX', 'ADI', 'MCO', 'EYEN', 'LPSN', 'DGX', 'AMRN', 'CWST', 'AVID', 'PCTY', 'RHI', 'WBT', 'LQDA', 'TRI', 'HLIT', 'LUNA', 'MIRM', 'SPWR', 'DT', 'IRM', 'NBRV', 'TRVI', 'LIFE', 'SAIL', 'VECO', 'SKM', 'SNA', 'SNPS', 'AIM', 'FND', 'CRM', 'CBAY', 'CPRT', 'WM', 'AGR', 'TGP', 'SPGI', 'JKS', 'DECK', 'ROK', 'CRSP', 'NTRA', 'RVNC', 'VIVO', 'CAJ', 'AKAM', 'GILD', 'SEDG', 'LLY', 'VRSK', 'TSM', 'ALDX', 'PLAB', 'SAIA', 'XCUR', 'INVA', 'WNC', 'HRC', 'WDC', 'SXTC', 'SPPI', 'MIC', 'VNE', 'ACIU', 'ATNX', 'ATOM', 'CLXT', 'CWEN', 'FOSL', 'GMDA', 'HEPA', 'LOGC', 'XPEL', 'HPE', 'KOF', 'FATE', 'KLAC', 'NEP', 'CDNS', 'DAVA', 'SBAC', 'NXST', 'OPRX', 'ROG', 'ZIXI', 'NUAN', 'FLO', 'ADAP', 'AMSC', 'IRTC', 'ZBRA', 'VIPS', 'DRNA', 'RMNI', 'MOH', 'MRK', 'BRKR', 'MRTN', 'NVCN', 'TWST', 'EYE', 'INTU', 'FMX', 'IT', 'FLGT', 'RMBS', 'MTSI', 'LH', 'RSG', 'BLFS', 'TRMB', 'TSCO', 'CLX', 'BGS', 'EDU', 'GRMN', 'TREX', 'IEP', 'ADPT', 'SPLK', 'ZTS', 'EQIX', 'FTCH', 'QCOM', 'VG', 'CHRS', 'QLYS', 'ZTO', 'STNE', 'VRNT', 'BLL', 'PRGS', 'TUFN', 'MAS', 'RCUS', 'TGLS', 'PERI', 'VNDA', 'FTAI', 'INFN', 'ATRA', 'TSLA', 'WB', 'PRFT', 'GENE', 'DLTH', 'MRTX', 'SMED', 'CAMT', 'TTWO', 'NKE', 'FLDM', 'DBX', 'RDUS', 'LXRX', 'KZR', 'NVMI', 'OVID', 'MOV', 'APPN', 'ARCB', 'FRPT', 'GMAB', 'VRAY', 'WOW', 'VZ', 'PPSI', 'PKI', 'NPTN', 'URGN', 'INCY', 'DDS', 'HAIN', 'KLIC', 'AQST', 'DIOD', 'IMMR', 'CTK', 'PBYI', 'XERS', 'ELP', 'CRMD', 'NXPI', 'DPZ', 'T', 'CBD', 'BNGO', 'XNCR', 'CKPT', 'FIXX', 'MANH', 'BCC', 'WSM', 'ONCT', 'SUPN', 'HPQ', 'ENTG', 'SRRK', 'CARA', 'MRSN', 'TNDM', 'BIMI', 'CDAY', 'NTLA', 'CHTR', 'REGN', 'MCHP', 'ALLO', 'PETS', 'KRYS', 'TPTX', 'NYT', 'CEMI', 'AZRE', 'CASI', 'AKTS', 'VHC', 'CTLT', 'REDU', 'EBAY', 'GTES', 'NEWR', 'VAPO', 'HEAR', 'HZNP', 'SQ', 'ARGX', 'SRAX', 'CERS', 'ENPH', 'NTAP', 'AZPN', 'GME', 'MXL', 'SONO', 'XLNX', 'VIV', 'ATEN', 'REPL', 'QGEN', 'ZYME', 'CROX', 'SITE', 'BBY', 'YNDX', 'FDS', 'ZUO', 'CLLS', 'CRWD', 'STX', 'TGT', 'ODFL', 'CRL', 'KAR', 'ASML', 'ETSY', 'GRFS', 'ITCI', 'CYAD', 'NVDA', 'BCRX', 'WST', 'TTM', 'KERN', 'TW', 'HHR', 'DHR', 'PRVB', 'VNET', 'JD', 'MGTA', 'AFYA', 'KEYS', 'PHR', 'VCRA', 'CMBM', 'YCBD', 'NICE', 'ICLR', 'PODD', 'PSTI', 'TMO', 'AXDX', 'AOSL', 'BTAI', 'ARWR', 'TOPS', 'TAL', 'LULU', 'INFY', 'RRD', 'SGEN', 'LE', 'CDMO', 'VMW', 'KRNT', 'CSTL', 'GNCA', 'APLS', 'ON', 'PETQ', 'ESTC', 'OSS', 'CDXS', 'QTT', 'SNCR', 'SE', 'FTNT', 'DKS', 'MGTX', 'CCRN', 'ACMR', 'APEN', 'CRTX', 'BEAT', 'JOBS', 'AMD', 'EPAM', 'PANW', 'UBX', 'COCP', 'GH', 'ZLAB', 'XFOR', 'ASYS', 'KALA', 'BLRX', 'JACK', 'TH', 'SIGA', 'SONM', 'MDB', 'HUBS', 'BHVN', 'ECOR', 'AGIO', 'MOR', 'ALLK', 'CUE', 'BCYC', 'HOTH', 'CHWY', 'BSGM', 'ICAD', 'AGMH', 'W', 'IDYA', 'SPWH', 'MSTR', 'PFE', 'QDEL', 'ARCT', 'GRUB', 'SEAC', 'GLOP', 'PLXP', 'PRTA', 'FENC', 'GNRC', 'BGNE', 'CANF', 'MCRB', 'RGEN', 'BIG', 'MPWR', 'NERV', 'WORX', 'POWI', 'NEON', 'AGE', 'MRAM', 'WIRE', 'SINT', 'ENTA', 'GRTS', 'HCM', 'ARDX', 'OPNT', 'YJ', 'NVAX', 'VICR', 'USX', 'UI', 'VRNA', 'TXMD', 'MRNA', 'ZS', 'COE', 'BEDU', 'TC', 'CTMX', 'NTP', 'SECO', 'AGLE', 'RETA']

today = datetime.datetime.today()

amounts_days = datetime.timedelta(days=30)
start = (today-amounts_days).strftime("%Y-%m-%d")
print(start)

end = today.strftime("%Y-%m-%d")
print(end)
def finding_tickers(ticker):
    df_yahoo = yf.download(
                ticker,
                start=start,
                end=end,
                progress=False)

    data = yf.download(tickers=ticker,
                       period='30m',
                       progress=False,
                       interval='5m')
    df_yahoo = df_yahoo.reset_index()
    data = data.reset_index()

    try:
        avg_vol_3_5 = int(mean(list(df_yahoo.iloc[-3:, 6])) * 5 / 1440)
        present_price = int(mean(list(data.iloc[-4:-1, 6])))
        if avg_vol_3_5 * 3 <= present_price: # if 3days 5min volume * 3 <= real time volume
            print(ticker)

    except:
        print(f'no data {ticker}')

for i in list_ticks:
    finding_tickers(i)
print('The End')
# df_yahoo = yf.download(
#                 'HUYA',
#                 start=start,
#                 end=end,
#                 progress=False)
#
# data = yf.download(tickers='HUYA',
#                    period='30m',
#                    progress=False,
#                    interval='5m')
# df_yahoo = df_yahoo.reset_index()
# Vol_3 = int(mean(list(df_yahoo.iloc[-3:, 6])) * 5 / 1440)
# # Vol_3_5 = int(Vol_3 * 5 / 1440)
# data = data.reset_index()
# present_price_3 = mean(list(data.iloc[-4:-1, 6]))
# # pr_pr = mean(present_price_3)
#
# print(Vol_3)
# # print(mean(Vol_3))
# print(present_price_3)
# print(data)
# print(df_yahoo)

#avg_3 =
# data = []
#
# while True:
#   st_th = threading.active_count()
#   time.sleep(3)
#   st_th2 = threading.active_count()
#   if st_th == st_th2:
#     break
#
# def scan_ticks(ticker, num):
#     while True:
#         try:
#             df_yahoo = yf.download(
#             ticker,
#             start=start,
#             end=end,
#             progress=False)
#
#             if len(df_yahoo.index) > 0:
#                 #print(f'\n {num} {ticker} Data OK!')
#                 break
#
#             else:
#                 #print(f'{ticker} Ожидание данных.')
#                 time.sleep(5)
#
#         except:
#             #print(f'{ticker} Ожидание данных.')
#             time.sleep(5)
#
#     dney = 30
#     v = 500000  # Средний объем
#     l = 19  # Нижняя цена
#
#
#
#     df_yahoo['Volat'] = df_yahoo['High'] - df_yahoo['Low']
#     volat = df_yahoo['Volat'].sum()
#
#     high_volat = df_yahoo['Volat'].max()
#     low_volat = df_yahoo['Volat'].min()
#     atr = (volat - high_volat - low_volat) / (dney - 2)
#
#     vol = df_yahoo['Volume'].sum()
#
#     high_volume = df_yahoo['Volume'].max()
#     low_volume = df_yahoo['Volume'].min()
#
#     #highest(volume(period=agg)[iBar], dney)
#     #lowest(volume(period=agg)[iBar], dney)
#
#     volum = (vol - high_volume - low_volume) / (dney - 2)
#
#     high = round(df_yahoo['High'].iloc[-1], 2)
#     low = round(df_yahoo['Low'].iloc[-1], 2)
#     close = round(df_yahoo['Close'].iloc[-1], 2)
#     volume = round(df_yahoo['Volume'].iloc[-1], 2)
#
#     # print('\n')
#     # print(f'{close} > {l}')
#     # print(f'{close} < {h}')
#     # print(f'{atr} > {a}')
#     #
#     # print(f'{volum} > {v}')
#     # print(f'{high - low} < {atr * pa}')
#     # print(f'{volume} > {volum * pv}')
#
#     a = datetime.datetime.now()
#     a.hour
#     a.minute
#
#     a = datetime.datetime.today().strftime("%H%M")
#
#     if int(a) <= 1830:
#         # Скринер до 10: 30:
#         h = 151;  # Верхняя цена
#         a = 0.5;  # ATR
#         pv = 0.5;  # % от среднего объема
#         pa = 0.5;  # % от atr
#         times = 'До 10:30'
#
#     else:
#         # Скринер после 10: 30:
#         h = 151  # Верхняя цена
#         a = 0.5  # ATR
#         pv = 0.9  # % от среднего объема
#         pa = 0.8  # % от atr
#         times = 'После 10:30'
#
#     if close > l and \
#             close < h and \
#             atr > a and \
#             volum > v and \
#             high-low > atr * pa and \
#             volume > volum * pv:
#         print(f'\n{ticker} - {times}')
#         data.append([ticker, close, times])
#
#     # Скринер акций которые вчера были активны:
#     h = 81  # Верхняя цена
#     a = 0.5  # ATR
#     pv = 1.5  # % от среднего объема
#     pa = 1.5  # % от atr
#
#     if close > l and \
#             close < h and \
#             atr > a and \
#             volum > v and \
#             high-low > atr * pa and \
#             volume > volum * pv:
#         print(f'\n{ticker} - Yestoday')
#
#
#         #avg_vol = ((f'{avg_vol:,}').replace(',', ' '))
#         data.append([ticker, close, 'Yestoday'])
#
#     #print(f'\n {num} {ticker} is END!')
#
# list_ticks = list_ticks[:500] ########################################## убрать строку после тестов
#
# n = 1
# for l in tqdm(list_ticks):
#     #threading.Thread(target=scan_ticks, args=(l, n, )).start()
#     scan_ticks(l, n)
#     #time.sleep(0.4)
#
#     n += 1
#
# n = 1
# while n < 50:
#     if threading.active_count() == st_th+1:
#       break
#     print('\nКол-во потоков: ', threading.active_count())
#     time.sleep(5)
#     n += 1
#
# if len(data) > 0:
#     df = pd.DataFrame(data)
#     df = df.sort_values(by=0, ascending=False).reset_index(drop=True)
#     #df[1] = df[1].apply('{:,}'.format)
#     print(df)
#
# else:
#     print('Подходящих акций не найдено((')
#
#
#
#     #scan_ticks(l)
