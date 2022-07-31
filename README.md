# Refrigerasi Module
This is refrigeration equation and prop module. Use it to your simulation

Here are some refrigeration prop lies in this module:
| Prop      | input param                                                         | output param |
| --------- | ------------                                                        | -----        |
| Generator | m<sub>in</sub>, h<sub>in</sub>, T<sub>in</sub>, X<sub>in</sub>, SCR | m<sub>out1</sub>, m<sub>out2</sub>, X<sub>out</sub> |
| Condenser | m<sub>in</sub>, h<sub>in</sub>, T<sub>in</sub>                      | m<sub>out</sub>, h<sub>out</sub>, T<sub>out</sub>, Q<sub>cond</sub> |
| Evaporator| m<sub>in</sub>, h<sub>in</sub>, T<sub>in</sub>,                     | m<sub>out</sub>, h<sub>out</sub>, T<sub>out</sub> |
| Absorber  | m<sub>in1</sub>, m<sub>in2</sub>, h<sub>in1</sub>, h<sub>in2</sub>, T<sub>in1</sub>, T<sub>in2</sub>, X<sub>in</sub>| m<sub>out</sub>, h<sub>out</sub>, T<sub>out</sub> |

**Using this module in python notebook / google colab, use this on the first code cell:**

    !git clone https://github.com/putraaryawinata/refrigerasi_module.git
    !cp refrigerasi_module/refrigerasi.py ./refrigerasi.py
    !pip install -r ./refrigerasi_module/requirements.txt

For further examples, look up on this google colab file [Refrigerasi.ipynb](https://colab.research.google.com/drive/1j23EkTVgXLsldmrEhr-A79fl5JC5URJ6#scrollTo=5ym3RoWtsSNL)
