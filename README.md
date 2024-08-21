# Rayleigh-LUT-for-ocean-color
通用瑞利散射查找表

当前水色遥感精确瑞利散射计算通常采用查找表方式进行，但由于这些查找表是针对特定遥感器生成，难以直接应用于新的水色遥感器。为此，我们利用自主研发的海洋-大气耦合矢量辐射传输模型PCOART，生成了通用的水色遥感精确瑞利散射查找表。通过与SeaDAS精确瑞利散射查找表结果比较，本通用查找表的计算精度优于0.5%，可用于所有水色遥感器的精确瑞利散射计算（适用范围为瑞利散射光学厚度小于0.4）。

使用本查找表，请引用如下文献：

>[1] Xianqiang He; Delu Pan; Yan Bai; Fang Gong. A general purpose exact Rayleigh scattering look-up table for ocean color remote sensing. Acta Oceanologica Sinica, 2006, 25(1): 48~56.

>[2] Xianqiang He; Yan Bai; Qiankun Zhu; Fang Gong. A vector radiative transfer model of coupled ocean-atmosphere system using matrix-operator method for rough sea-surface. Journal of Quantitative Spectroscopy and Radiative Transfer, 2010, 111(10): 1426~1448.

Matlab code: https://www.satco2.com/rjxz/gjbxz/tsbb/