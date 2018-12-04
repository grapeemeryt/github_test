#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["font.family"] = "Serif"
matplotlib.rcParams["font.size"] = 10
matplotlib.rcParams["axes.labelsize"] = 10
matplotlib.rcParams["xtick.labelsize"] = 10
matplotlib.rcParams["ytick.labelsize"] = 10
matplotlib.rcParams["legend.fontsize"] = 10

fig = plt.figure(figsize=(20,10),facecolor="white")
ax = fig.gca()
ax.grid()
ax.set_axisbelow(True)
ax.set_xlabel("angle (rad)")
ax.set_title("plot test")

x = np.array([0.0000000000000000E+00,0.2000000000000000E+00,0.4000000000000000E+00,0.6000000000000000E+00,0.8000000000000000E+00,0.1000000000000000E+01,0.1200000000000000E+01,0.1400000000000000E+01,0.1600000000000000E+01,0.1800000000000000E+01,0.2000000000000000E+01,0.2200000000000000E+01,0.2400000000000000E+01,0.2600000000000000E+01,0.2800000000000000E+01,0.3000000000000000E+01,0.3200000000000000E+01,0.3400000000000000E+01,0.3600000000000000E+01,0.3800000000000000E+01,0.4000000000000000E+01,0.4200000000000000E+01,0.4400000000000000E+01,0.4600000000000000E+01,0.4800000000000000E+01,0.5000000000000000E+01,0.5200000000000000E+01,0.5400000000000000E+01,0.5600000000000000E+01,0.5800000000000000E+01,0.6000000000000000E+01,0.6200000000000000E+01,0.6400000000000000E+01,0.6600000000000000E+01,0.6800000000000000E+01,0.7000000000000000E+01,0.7200000000000000E+01,0.7400000000000000E+01,0.7600000000000000E+01,0.7800000000000000E+01,0.8000000000000000E+01,0.8199999999999999E+01,0.8400000000000000E+01,0.8600000000000000E+01,0.8800000000000001E+01,0.9000000000000000E+01,0.9199999999999999E+01,0.9400000000000000E+01,0.9600000000000000E+01,0.9800000000000001E+01,0.1000000000000000E+02,0.1020000000000000E+02,0.1040000000000000E+02,0.1060000000000000E+02,0.1080000000000000E+02,0.1100000000000000E+02,0.1120000000000000E+02,0.1140000000000000E+02,0.1160000000000000E+02,0.1180000000000000E+02,0.1200000000000000E+02,0.1220000000000000E+02,0.1240000000000000E+02,0.1260000000000000E+02,0.1280000000000000E+02,0.1300000000000000E+02,0.1320000000000000E+02,0.1340000000000000E+02,0.1360000000000000E+02,0.1380000000000000E+02,0.1400000000000000E+02,0.1420000000000000E+02,0.1440000000000000E+02,0.1460000000000000E+02,0.1480000000000000E+02,0.1500000000000000E+02,0.1520000000000000E+02,0.1540000000000000E+02,0.1560000000000000E+02,0.1580000000000000E+02,0.1600000000000000E+02,0.1620000000000000E+02,0.1640000000000000E+02,0.1660000000000000E+02,0.1680000000000000E+02,0.1700000000000000E+02,0.1720000000000000E+02,0.1740000000000000E+02,0.1760000000000000E+02,0.1780000000000000E+02,0.1800000000000000E+02,0.1820000000000000E+02,0.1840000000000000E+02,0.1860000000000000E+02,0.1880000000000000E+02,0.1900000000000000E+02,0.1920000000000000E+02,0.1940000000000000E+02,0.1960000000000000E+02,0.1980000000000000E+02])
y = np.array([0.0000000000000000E+00,0.1986693307950612E+00,0.3894183423086505E+00,0.5646424733950354E+00,0.7173560908995228E+00,0.8414709848078965E+00,0.9320390859672263E+00,0.9854497299884601E+00,0.9995736030415051E+00,0.9738476308781951E+00,0.9092974268256817E+00,0.8084964038195901E+00,0.6754631805511510E+00,0.5155013718214642E+00,0.3349881501559051E+00,0.1411200080598672E+00,-0.5837414342758009E-01,-0.2555411020268312E+00,-0.4425204432948525E+00,-0.6118578909427189E+00,-0.7568024953079282E+00,-0.8715757724135882E+00,-0.9516020738895160E+00,-0.9936910036334644E+00,-0.9961646088358407E+00,-0.9589242746631385E+00,-0.8834546557201531E+00,-0.7727644875559871E+00,-0.6312666378723216E+00,-0.4646021794137574E+00,-0.2794154981989259E+00,-0.8308940281749640E-01,0.1165492048504936E+00,0.3115413635133779E+00,0.4941133511386082E+00,0.6569865987187891E+00,0.7936678638491531E+00,0.8987080958116269E+00,0.9679196720314863E+00,0.9985433453746050E+00,0.9893582466233818E+00,0.9407305566797731E+00,0.8545989080882804E+00,0.7343970978741133E+00,0.5849171928917617E+00,0.4121184852417566E+00,0.2228899141002476E+00,0.2477542545335776E-01,-0.1743267812229796E+00,-0.3664791292519284E+00,-0.5440211108893698E+00,-0.6998746875935423E+00,-0.8278264690856537E+00,-0.9227754216128066E+00,-0.9809362300664916E+00,-0.9999902065507035E+00,-0.9791777291513174E+00,-0.9193285256646757E+00,-0.8228285949687089E+00,-0.6935250847771224E+00,-0.5365729180004349E+00,-0.3582292822368287E+00,-0.1656041754483094E+00,0.3362304722113670E-01,0.2315098251015389E+00,0.4201670368266409E+00,0.5920735147072230E+00,0.7403758899524486E+00,0.8591618148564958E+00,0.9436956694441048E+00,0.9906073556948704E+00,0.9980266527163617E+00,0.9656577765492774E+00,0.8947911721405042E+00,0.7882520673753163E+00,0.6502878401571168E+00,0.4863986888537997E+00,0.3031183567457023E+00,0.1077536522994441E+00,-0.9190685022768164E-01,-0.2879033166650653E+00,-0.4724219863984662E+00,-0.6381066823479474E+00,-0.7783520785342984E+00,-0.8875670335815046E+00,-0.9613974918795568E+00,-0.9969000660415961E+00,-0.9926593804706332E+00,-0.9488444979181240E+00,-0.8672021794855813E+00,-0.7509872467716761E+00,-0.6048328224062841E+00,-0.4345656220718968E+00,-0.2469736617366209E+00,-0.4953564087836742E-01,0.1498772096629523E+00,0.3433149288198954E+00,0.5230657651576964E+00,0.6819636200681356E+00,0.8136737375071054E+00])

ax.plot(x,y,"b-o",linewidth=2,markersize=5,label="$\sin (x)$")

x = np.array([0.0000000000000000E+00,0.2000000000000000E+00,0.4000000000000000E+00,0.6000000000000000E+00,0.8000000000000000E+00,0.1000000000000000E+01,0.1200000000000000E+01,0.1400000000000000E+01,0.1600000000000000E+01,0.1800000000000000E+01,0.2000000000000000E+01,0.2200000000000000E+01,0.2400000000000000E+01,0.2600000000000000E+01,0.2800000000000000E+01,0.3000000000000000E+01,0.3200000000000000E+01,0.3400000000000000E+01,0.3600000000000000E+01,0.3800000000000000E+01,0.4000000000000000E+01,0.4200000000000000E+01,0.4400000000000000E+01,0.4600000000000000E+01,0.4800000000000000E+01,0.5000000000000000E+01,0.5200000000000000E+01,0.5400000000000000E+01,0.5600000000000000E+01,0.5800000000000000E+01,0.6000000000000000E+01,0.6200000000000000E+01,0.6400000000000000E+01,0.6600000000000000E+01,0.6800000000000000E+01,0.7000000000000000E+01,0.7200000000000000E+01,0.7400000000000000E+01,0.7600000000000000E+01,0.7800000000000000E+01,0.8000000000000000E+01,0.8199999999999999E+01,0.8400000000000000E+01,0.8600000000000000E+01,0.8800000000000001E+01,0.9000000000000000E+01,0.9199999999999999E+01,0.9400000000000000E+01,0.9600000000000000E+01,0.9800000000000001E+01,0.1000000000000000E+02,0.1020000000000000E+02,0.1040000000000000E+02,0.1060000000000000E+02,0.1080000000000000E+02,0.1100000000000000E+02,0.1120000000000000E+02,0.1140000000000000E+02,0.1160000000000000E+02,0.1180000000000000E+02,0.1200000000000000E+02,0.1220000000000000E+02,0.1240000000000000E+02,0.1260000000000000E+02,0.1280000000000000E+02,0.1300000000000000E+02,0.1320000000000000E+02,0.1340000000000000E+02,0.1360000000000000E+02,0.1380000000000000E+02,0.1400000000000000E+02,0.1420000000000000E+02,0.1440000000000000E+02,0.1460000000000000E+02,0.1480000000000000E+02,0.1500000000000000E+02,0.1520000000000000E+02,0.1540000000000000E+02,0.1560000000000000E+02,0.1580000000000000E+02,0.1600000000000000E+02,0.1620000000000000E+02,0.1640000000000000E+02,0.1660000000000000E+02,0.1680000000000000E+02,0.1700000000000000E+02,0.1720000000000000E+02,0.1740000000000000E+02,0.1760000000000000E+02,0.1780000000000000E+02,0.1800000000000000E+02,0.1820000000000000E+02,0.1840000000000000E+02,0.1860000000000000E+02,0.1880000000000000E+02,0.1900000000000000E+02,0.1920000000000000E+02,0.1940000000000000E+02,0.1960000000000000E+02,0.1980000000000000E+02])
y = np.array([0.1000000000000000E+01,0.9800665778412416E+00,0.9210609940028851E+00,0.8253356149096783E+00,0.6967067093471654E+00,0.5403023058681398E+00,0.3623577544766736E+00,0.1699671429002410E+00,-0.2919952230128882E-01,-0.2272020946930871E+00,-0.4161468365471424E+00,-0.5885011172553458E+00,-0.7373937155412454E+00,-0.8568887533689473E+00,-0.9422223406686581E+00,-0.9899924966004454E+00,-0.9982947757947531E+00,-0.9667981925794611E+00,-0.8967584163341470E+00,-0.7909677119144168E+00,-0.6536436208636119E+00,-0.4902608213406994E+00,-0.3073328699784194E+00,-0.1121525269350549E+00,0.8749898343944640E-01,0.2836621854632262E+00,0.4685166713003771E+00,0.6346928759426347E+00,0.7755658785102496E+00,0.8855195169413189E+00,0.9601702866503660E+00,0.9965420970232175E+00,0.9931849187581926E+00,0.9502325919585296E+00,0.8693974903498253E+00,0.7539022543433046E+00,0.6083513145322546E+00,0.4385473275743904E+00,0.2512598425822557E+00,0.5395542056264975E-01,-0.1455000338086135E+00,-0.3391548609838345E+00,-0.5192886541166856E+00,-0.6787200473200125E+00,-0.8110930140616560E+00,-0.9111302618846769E+00,-0.9748436214041636E+00,-0.9996930420352065E+00,-0.9846878557941270E+00,-0.9304262721047533E+00,-0.8390715290764524E+00,-0.7142656520272003E+00,-0.5609842574272288E+00,-0.3853381907718296E+00,-0.1943299064553348E+00,0.4425697988050785E-02,0.2030048638187504E+00,0.3934908663478909E+00,0.5682896297679736E+00,0.7204324789908387E+00,0.8438539587324921E+00,0.9336336440746373E+00,0.9861923022788637E+00,0.9994345855010047E+00,0.9728325656974354E+00,0.9074467814501962E+00,0.8058839576404507E+00,0.6721930835534681E+00,0.5117039924531490E+00,0.3308148779490470E+00,0.1367372182078336E+00,-0.6279172292408176E-01,-0.2598173562137558E+00,-0.4464848914122656E+00,-0.6153524829547208E+00,-0.7596879128588213E+00,-0.8737369830110802E+00,-0.9529529168871803E+00,-0.9941776251838151E+00,-0.9957676088732885E+00,-0.9576594803233847E+00,-0.8813724903622346E+00,-0.7699479605420717E+00,-0.6278280352463860E+00,-0.4606785874113625E+00,-0.2751633380515969E+00,-0.7867819473184015E-01,0.1209435999284741E+00,0.3157437549192433E+00,0.4979562027884155E+00,0.6603167082440802E+00,0.7963524702919231E+00,0.9006401723847685E+00,0.9690221929390499E+00,0.9987723565872102E+00,0.9887046181866692E+00,0.9392203466968708E+00,0.8522923238654644E+00,0.7313860956454967E+00,0.5813218118144357E+00])

ax.plot(x,y,"r-o",linewidth=2,markersize=5,label="$\cos (x)$")

x = np.array([0.0000000000000000E+00,0.2000000000000000E+00,0.4000000000000000E+00,0.6000000000000000E+00,0.8000000000000000E+00,0.1000000000000000E+01,0.1200000000000000E+01,0.1400000000000000E+01,0.1600000000000000E+01,0.1800000000000000E+01,0.2000000000000000E+01,0.2200000000000000E+01,0.2400000000000000E+01,0.2600000000000000E+01,0.2800000000000000E+01,0.3000000000000000E+01,0.3200000000000000E+01,0.3400000000000000E+01,0.3600000000000000E+01,0.3800000000000000E+01,0.4000000000000000E+01,0.4200000000000000E+01,0.4400000000000000E+01,0.4600000000000000E+01,0.4800000000000000E+01,0.5000000000000000E+01,0.5200000000000000E+01,0.5400000000000000E+01,0.5600000000000000E+01,0.5800000000000000E+01,0.6000000000000000E+01,0.6200000000000000E+01,0.6400000000000000E+01,0.6600000000000000E+01,0.6800000000000000E+01,0.7000000000000000E+01,0.7200000000000000E+01,0.7400000000000000E+01,0.7600000000000000E+01,0.7800000000000000E+01,0.8000000000000000E+01,0.8199999999999999E+01,0.8400000000000000E+01,0.8600000000000000E+01,0.8800000000000001E+01,0.9000000000000000E+01,0.9199999999999999E+01,0.9400000000000000E+01,0.9600000000000000E+01,0.9800000000000001E+01,0.1000000000000000E+02,0.1020000000000000E+02,0.1040000000000000E+02,0.1060000000000000E+02,0.1080000000000000E+02,0.1100000000000000E+02,0.1120000000000000E+02,0.1140000000000000E+02,0.1160000000000000E+02,0.1180000000000000E+02,0.1200000000000000E+02,0.1220000000000000E+02,0.1240000000000000E+02,0.1260000000000000E+02,0.1280000000000000E+02,0.1300000000000000E+02,0.1320000000000000E+02,0.1340000000000000E+02,0.1360000000000000E+02,0.1380000000000000E+02,0.1400000000000000E+02,0.1420000000000000E+02,0.1440000000000000E+02,0.1460000000000000E+02,0.1480000000000000E+02,0.1500000000000000E+02,0.1520000000000000E+02,0.1540000000000000E+02,0.1560000000000000E+02,0.1580000000000000E+02,0.1600000000000000E+02,0.1620000000000000E+02,0.1640000000000000E+02,0.1660000000000000E+02,0.1680000000000000E+02,0.1700000000000000E+02,0.1720000000000000E+02,0.1740000000000000E+02,0.1760000000000000E+02,0.1780000000000000E+02,0.1800000000000000E+02,0.1820000000000000E+02,0.1840000000000000E+02,0.1860000000000000E+02,0.1880000000000000E+02,0.1900000000000000E+02,0.1920000000000000E+02,0.1940000000000000E+02,0.1960000000000000E+02,0.1980000000000000E+02])
y = np.array([0.0000000000000000E+00,0.1947091711543252E+00,0.3586780454497614E+00,0.4660195429836132E+00,0.4997868015207526E+00,0.4546487134128409E+00,0.3377315902755755E+00,0.1674940750779526E+00,-0.2918707171379004E-01,-0.2212602216474262E+00,-0.3784012476539642E+00,-0.4758010369447580E+00,-0.4980823044179203E+00,-0.4417273278600766E+00,-0.3156333189361608E+00,-0.1397077490994629E+00,0.5827460242524683E-01,0.2470566755693041E+00,0.3968339319245766E+00,0.4839598360157432E+00,0.4946791233116909E+00,0.4272994540441403E+00,0.2924585964458808E+00,0.1114449570501238E+00,-0.8716339061148982E-01,-0.2720105554446849E+00,-0.4139132345428268E+00,-0.4904681150332458E+00,-0.4895888645756587E+00,-0.4114142974843544E+00,-0.2682864590002175E+00,-0.8280208772415469E-01,0.1157549125507695E+00,0.2960367573536115E+00,0.4295809074282479E+00,0.4953036778474351E+00,0.4828288882746387E+00,0.3941260336876581E+00,0.2431993444268998E+00,0.5387682614972204E-01,-0.1439516583325327E+00,-0.3190533411739737E+00,-0.4437835167907522E+00,-0.4984500330207980E+00,-0.4744222489590620E+00,-0.3754936233858380E+00,-0.2172828110359483E+00,-0.2476782043918371E-01,0.1716574644099477E+00,0.3409818100340678E+00,0.4564726253638138E+00,0.4998964500713346E+00,0.4643976170386202E+00,0.3555806114529912E+00,0.1906252458274701E+00,-0.4425654645201938E-02,-0.1987778415607165E+00,-0.3617473780221225E+00,-0.4676049575972694E+00,-0.4996379960683139E+00,-0.4527891810033119E+00,-0.3344549101890121E+00,-0.1633175630523611E+00,0.3360403626273746E-01,0.2252202971376946E+00,0.3812792252398013E+00,0.4771425472463485E+00,0.4976755524557796E+00,0.4396365308253621E+00,0.3121885677081957E+00,0.1354528941539345E+00,-0.6266781304821456E-01,-0.2508946505102870E+00,-0.3995107393298069E+00,-0.4850528668535927E+00,-0.4940158120464309E+00,-0.4249845229396640E+00,-0.2888575222228659E+00,-0.1071262701479438E+00,0.9151786449029399E-01,0.2757133406208453E+00,0.4163797426538899E+00,0.4913089386820697E+00,0.4886712561961293E+00,0.4088831272632209E+00,0.2645413430600119E+00,0.7843429752420500E-01,-0.1200557989768873E+00,-0.2995917246071326E+00,-0.4318287043464780E+00,-0.4958894267215578E+00,-0.4816601122368804E+00,-0.3913872567753272E+00,-0.2393229592942075E+00,-0.4947482877514477E-01,0.1481842893546927E+00,0.3224483664724337E+00,0.4458049365207203E+00,0.4987787094539026E+00,0.4730062913134540E+00])

ax.plot(x,y,"g-o",linewidth=1,markersize=2,label="$\sin (x) \cos (x)$")

ax.legend(loc="best")

ax.axis("equal")

fig.tight_layout()

plt.savefig("plottest.png")

