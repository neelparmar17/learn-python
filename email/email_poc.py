import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "neel.parmar@trringo.com"
receiver = "jyothi.gurung@trringo.com"

msg = MIMEMultipart("alternative")
msg["Subject"] = "test email from python"
msg["From"] = sender
msg["To"] = receiver

# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
html = """\
<html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: center;    
        }
        </style>
    <title>Document</title>
    </head>
    <body>
    <table>
        <tr>
        <th rowspan="3">State</th>
        <th rowspan="3">Hub</th>
        <th colspan="5">MTD(07/03/2018)</th>
        </tr>
        <tr>
        <th colspan="2">Tractor+Harvestor</th>
        <th colspan="2">Implement only</th>
        <th colspan="1">Registered farmers</th>
        </tr>
        <tr>
        <td>completed Hrs</td>
        <td>count</td>
        <td>completed Hrs</td>
        <td>count</td>
        <td>count</td>
        </tr>
        <tr>
        <td>Total</td>
        <td></td>
        <td>1765.0</td>
        <td>421</td>
        <td>64.0</td>
        <td>4</td>
        <td>507</td>
        </tr>
        
                <tr>
                    <td rowspan = 44>
                        Karnataka
                    </td>
                    <td bgcolor = #fbf193>Total</td>
                    <td bgcolor = #fbf193>1557.0</td>
                    <td bgcolor = #fbf193>360</td>
                    <td bgcolor = #fbf193>64.0</td>
                    <td bgcolor = #fbf193>4</td>
                    <td bgcolor = #fbf193>398</td>
                    </tr>
            
                        <tr>
                            <td bgcolor= "#fb9393">
                                Chikkayanachatra
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Kurugodu
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Sulepeth
                            </td>
                            <td>
                                123.0
                            </td>
                            <td>
                                16
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                2
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Hampapura
                            </td>
                            <td>
                                42.0
                            </td>
                            <td>
                                18
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                19
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Kasaba(Kollegal)
                            </td>
                            <td>
                                16.0
                            </td>
                            <td>
                                15
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                5
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Gillesugur
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                5
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Adaki
                            </td>
                            <td>
                                160.0
                            </td>
                            <td>
                                14
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                3
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Jayapura
                            </td>
                            <td>
                                69.0
                            </td>
                            <td>
                                43
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                20
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Ramanathapura
                            </td>
                            <td>
                                19.0
                            </td>
                            <td>
                                12
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                3
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Madeehalli
                            </td>
                            <td>
                                9.0
                            </td>
                            <td>
                                4
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                92
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Mariyammanahalli
                            </td>
                            <td>
                                7.0
                            </td>
                            <td>
                                3
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Kampli
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                10
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Farhatabad
                            </td>
                            <td>
                                123.0
                            </td>
                            <td>
                                12
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                2
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Nelogi
                            </td>
                            <td>
                                74.0
                            </td>
                            <td>
                                14
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                4
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Kasaba(Channarayapatna)
                            </td>
                            <td>
                                12.0
                            </td>
                            <td>
                                8
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                54
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Kasaba(Periyapatna)
                            </td>
                            <td>
                                42.0
                            </td>
                            <td>
                                10
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Tekkalakote
                            </td>
                            <td>
                                16.0
                            </td>
                            <td>
                                2
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                2
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Kasaba(Holenarasipura)
                            </td>
                            <td>
                                19.0
                            </td>
                            <td>
                                7
                            </td>
                            <td>
                                8.0
                            </td>
                            <td>
                                1
                            </td>
                            <td>
                                9
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Narona
                            </td>
                            <td>
                                155.0
                            </td>
                            <td>
                                13
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                8
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Mudhol
                            </td>
                            <td>
                                58.0
                            </td>
                            <td>
                                8
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Kandalike
                            </td>
                            <td>
                                27.0
                            </td>
                            <td>
                                19
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Pattan
                            </td>
                            <td>
                                117.0
                            </td>
                            <td>
                                14
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                7
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Terakanambi
                            </td>
                            <td>
                                79.0
                            </td>
                            <td>
                                25
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                5
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Andola
                            </td>
                            <td>
                                86.0
                            </td>
                            <td>
                                16
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                6
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Talakadu
                            </td>
                            <td>
                                32.0
                            </td>
                            <td>
                                7
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                17
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Saligrama
                            </td>
                            <td>
                                24.0
                            </td>
                            <td>
                                4
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Elwala
                            </td>
                            <td>
                                6.0
                            </td>
                            <td>
                                2
                            </td>
                            <td>
                                40.0
                            </td>
                            <td>
                                1
                            </td>
                            <td>
                                67
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Hullahalli
                            </td>
                            <td>
                                56.0
                            </td>
                            <td>
                                29
                            </td>
                            <td>
                                8.0
                            </td>
                            <td>
                                1
                            </td>
                            <td>
                                4
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Karur
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Hunasagi
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                4
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Kembhavi
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Chittapur
                            </td>
                            <td>
                                62.0
                            </td>
                            <td>
                                10
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                15
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Salagame
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Udigala(Harave)
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Gowdagere
                            </td>
                            <td>
                                1.0
                            </td>
                            <td>
                                1
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                11
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Hitnal
                            </td>
                            <td>
                                8.0
                            </td>
                            <td>
                                2
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                5
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Haranahalli
                            </td>
                            <td>
                                29.0
                            </td>
                            <td>
                                13
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Goggi
                            </td>
                            <td>
                                39.0
                            </td>
                            <td>
                                9
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                4
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Tavargera
                            </td>
                            <td>
                                21.0
                            </td>
                            <td>
                                5
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Kalgi
                            </td>
                            <td>
                                20.0
                            </td>
                            <td>
                                2
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                2
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Siruguppa
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                8.0
                            </td>
                            <td>
                                1
                            </td>
                            <td>
                                3
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Kasaba(Hunsur)
                            </td>
                            <td>
                                7.0
                            </td>
                            <td>
                                3
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>

                        </tr>
                    
                <tr bgcolor = #9bc4ff>
                    <td>C2Cs on New Platform</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                </tr>
            
                <tr>
                    <td rowspan = 11>
                        Maharashtra
                    </td>
                    <td bgcolor = #fbf193>Total</td>
                    <td bgcolor = #fbf193>111.0</td>
                    <td bgcolor = #fbf193>31</td>
                    <td bgcolor = #fbf193>0</td>
                    <td bgcolor = #fbf193>0</td>
                    <td bgcolor = #fbf193>38</td>
                    </tr>
            
                        <tr>
                            <td bgcolor= "#ffffff">
                                Jawalga
                            </td>
                            <td>
                                43.0
                            </td>
                            <td>
                                4
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                2
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Kurhadi
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Satara
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Katpur
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Karad
                            </td>
                            <td>
                                15.0
                            </td>
                            <td>
                                9
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                7
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Budhoda
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                4
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Killari-Karkhana
                            </td>
                            <td>
                                16.0
                            </td>
                            <td>
                                2
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                10
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Killari
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                5
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Koregaon
                            </td>
                            <td>
                                34.0
                            </td>
                            <td>
                                14
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                7
                            </td>

                        </tr>
                    
                <tr bgcolor = #9bc4ff>
                    <td>C2Cs on New Platform</td>
                    <td>3.0</td>
                    <td>2</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                </tr>
            
                <tr>
                    <td rowspan = 4>
                        Madhya Pradesh
                    </td>
                    <td bgcolor = #fbf193>Total</td>
                    <td bgcolor = #fbf193>4.0</td>
                    <td bgcolor = #fbf193>1</td>
                    <td bgcolor = #fbf193>0</td>
                    <td bgcolor = #fbf193>0</td>
                    <td bgcolor = #fbf193>1</td>
                    </tr>
            
                        <tr>
                            <td bgcolor= "#ffffff">
                                Barkheda Bhogi
                            </td>
                            <td>
                                4.0
                            </td>
                            <td>
                                1
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Ghatiya
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                <tr bgcolor = #9bc4ff>
                    <td>C2Cs on New Platform</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                </tr>
            
                <tr>
                    <td rowspan = 3>
                        Rajasthan
                    </td>
                    <td bgcolor = #fbf193>Total</td>
                    <td bgcolor = #fbf193>0</td>
                    <td bgcolor = #fbf193>0</td>
                    <td bgcolor = #fbf193>0</td>
                    <td bgcolor = #fbf193>0</td>
                    <td bgcolor = #fbf193>1</td>
                    </tr>
            
                        <tr>
                            <td bgcolor= "#fb9393">
                                53 LNP
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                <tr bgcolor = #9bc4ff>
                    <td>C2Cs on New Platform</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                </tr>
            
                <tr>
                    <td rowspan = 8>
                        Gujarat
                    </td>
                    <td bgcolor = #fbf193>Total</td>
                    <td bgcolor = #fbf193>93.0</td>
                    <td bgcolor = #fbf193>29</td>
                    <td bgcolor = #fbf193>0</td>
                    <td bgcolor = #fbf193>0</td>
                    <td bgcolor = #fbf193>69</td>
                    </tr>
            
                        <tr>
                            <td bgcolor= "#ffffff">
                                Rampur
                            </td>
                            <td>
                                16.0
                            </td>
                            <td>
                                2
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Navalpur
                            </td>
                            <td>
                                13.0
                            </td>
                            <td>
                                2
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Gandhinagar
                            </td>
                            <td>
                                4.0
                            </td>
                            <td>
                                6
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                31
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#fb9393">
                                Bhukhel
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                7
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Alvakampa
                            </td>
                            <td>
                                18.0
                            </td>
                            <td>
                                3
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                1
                            </td>

                        </tr>
                    
                        <tr>
                            <td bgcolor= "#ffffff">
                                Dahegam
                            </td>
                            <td>
                                42.0
                            </td>
                            <td>
                                16
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                0
                            </td>
                            <td>
                                30
                            </td>

                        </tr>
                    
                <tr bgcolor = #9bc4ff>
                    <td>C2Cs on New Platform</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                </tr>
            </table>
    
    <br>
    <br>
    <br>
    <table>
        <tr>
        <th rowspan="2">State</th>
        <th rowspan="2">Hub</th>
        <th colspan="3">06/03/2018</th>
        <th colspan="3">MTD(07/03/2018)</th>
        </tr>
        <tr>
        <th>C2C</th>
        <th>Franchisee</th>
        <th>Total</th>
        <th>C2C</th>
        <th>Franchisee</th>
        <th>Total</th>
        </tr>
        <tr>
        <td>Total</td>
        <td></td>
        <td>66.0</td>
        <td>142.0</td>
        <td>208.0</td>
        <td>651.0</td>
        <td>1114.0</td>
        <td>1765.0</td>
        </tr>
    
            <tr>
                <td rowspan = 34>
                    Karnataka
                </td>
                <td bgcolor = #fbf193>Total</td>
                <td bgcolor = #fbf193>55.0</td>
                <td bgcolor = #fbf193>110.0</td>
                <td bgcolor = #fbf193>165.0</td>
                <td bgcolor = #fbf193>540.0</td>
                <td bgcolor = #fbf193>1016.0</td>
                <td bgcolor = #fbf193>1557.0</td>
            </tr>
            
                    <tr>
                        <td>Pattan</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>117.0</td>
                        <td>0</td>
                        <td>117.0</td>
                    </tr>
                    
                    <tr>
                        <td>Terakanambi</td>
                        <td>0</td>
                        <td>9.0</td>
                        <td>9.0</td>
                        <td>0</td>
                        <td>79.0</td>
                        <td>79.0</td>
                    </tr>
                    
                    <tr>
                        <td>Kalgi</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>20.0</td>
                        <td>20.0</td>
                    </tr>
                    
                    <tr>
                        <td>Kasaba(Periyapatna)</td>
                        <td>0</td>
                        <td>2.0</td>
                        <td>2.0</td>
                        <td>0</td>
                        <td>42.0</td>
                        <td>42.0</td>
                    </tr>
                    
                    <tr>
                        <td>Andola</td>
                        <td>8.0</td>
                        <td>4.0</td>
                        <td>12.0</td>
                        <td>77.0</td>
                        <td>9.0</td>
                        <td>86.0</td>
                    </tr>
                    
                    <tr>
                        <td>Sulepeth</td>
                        <td>0</td>
                        <td>5.0</td>
                        <td>5.0</td>
                        <td>56.0</td>
                        <td>67.0</td>
                        <td>123.0</td>
                    </tr>
                    
                    <tr>
                        <td>Chittapur</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>62.0</td>
                        <td>62.0</td>
                    </tr>
                    
                    <tr>
                        <td>Hampapura</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>42.0</td>
                        <td>42.0</td>
                    </tr>
                    
                    <tr>
                        <td>Kasaba(Kollegal)</td>
                        <td>1.0</td>
                        <td>4.0</td>
                        <td>5.0</td>
                        <td>3.0</td>
                        <td>14.0</td>
                        <td>16.0</td>
                    </tr>
                    
                    <tr>
                        <td>Saligrama</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>5.0</td>
                        <td>19.0</td>
                        <td>24.0</td>
                    </tr>
                    
                    <tr>
                        <td>Hullahalli</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>4.0</td>
                        <td>52.0</td>
                        <td>56.0</td>
                    </tr>
                    
                    <tr>
                        <td>Adaki</td>
                        <td>16.0</td>
                        <td>14.0</td>
                        <td>30.0</td>
                        <td>95.0</td>
                        <td>65.0</td>
                        <td>160.0</td>
                    </tr>
                    
                    <tr>
                        <td>Jayapura</td>
                        <td>0</td>
                        <td>19.0</td>
                        <td>19.0</td>
                        <td>0</td>
                        <td>69.0</td>
                        <td>69.0</td>
                    </tr>
                    
                    <tr>
                        <td>Ramanathapura</td>
                        <td>0</td>
                        <td>5.0</td>
                        <td>5.0</td>
                        <td>0</td>
                        <td>19.0</td>
                        <td>19.0</td>
                    </tr>
                    
                    <tr>
                        <td>Haranahalli</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>29.0</td>
                        <td>29.0</td>
                    </tr>
                    
                    <tr>
                        <td>Madeehalli</td>
                        <td>0</td>
                        <td>2.0</td>
                        <td>2.0</td>
                        <td>0</td>
                        <td>9.0</td>
                        <td>9.0</td>
                    </tr>
                    
                    <tr>
                        <td>Elwala</td>
                        <td>0</td>
                        <td>5.0</td>
                        <td>5.0</td>
                        <td>0</td>
                        <td>6.0</td>
                        <td>6.0</td>
                    </tr>
                    
                    <tr>
                        <td>Kandalike</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>27.0</td>
                        <td>27.0</td>
                    </tr>
                    
                    <tr>
                        <td>Tavargera</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>21.0</td>
                        <td>21.0</td>
                    </tr>
                    
                    <tr>
                        <td>Farhatabad</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>56.0</td>
                        <td>67.0</td>
                        <td>123.0</td>
                    </tr>
                    
                    <tr>
                        <td>Nelogi</td>
                        <td>10.0</td>
                        <td>6.0</td>
                        <td>16.0</td>
                        <td>20.0</td>
                        <td>54.0</td>
                        <td>74.0</td>
                    </tr>
                    
                    <tr>
                        <td>Hitnal</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>8.0</td>
                        <td>8.0</td>
                    </tr>
                    
                    <tr>
                        <td>Narona</td>
                        <td>20.0</td>
                        <td>20.0</td>
                        <td>40.0</td>
                        <td>75.0</td>
                        <td>80.0</td>
                        <td>155.0</td>
                    </tr>
                    
                    <tr>
                        <td>Goggi</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>39.0</td>
                        <td>39.0</td>
                    </tr>
                    
                    <tr>
                        <td>Kasaba(Channarayapatna)</td>
                        <td>0</td>
                        <td>1.0</td>
                        <td>1.0</td>
                        <td>0</td>
                        <td>12.0</td>
                        <td>12.0</td>
                    </tr>
                    
                    <tr>
                        <td>Tekkalakote</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>16.0</td>
                        <td>16.0</td>
                    </tr>
                    
                    <tr>
                        <td>Kasaba(Holenarasipura)</td>
                        <td>0</td>
                        <td>2.0</td>
                        <td>2.0</td>
                        <td>0</td>
                        <td>19.0</td>
                        <td>19.0</td>
                    </tr>
                    
                    <tr>
                        <td>Mariyammanahalli</td>
                        <td>0</td>
                        <td>4.0</td>
                        <td>4.0</td>
                        <td>0</td>
                        <td>7.0</td>
                        <td>7.0</td>
                    </tr>
                    
                    <tr>
                        <td>Mudhol</td>
                        <td>0</td>
                        <td>9.0</td>
                        <td>9.0</td>
                        <td>32.0</td>
                        <td>26.0</td>
                        <td>58.0</td>
                    </tr>
                    
                    <tr>
                        <td>Kasaba(Hunsur)</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>7.0</td>
                        <td>7.0</td>
                    </tr>
                    
                    <tr>
                        <td>Talakadu</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>32.0</td>
                        <td>32.0</td>
                    </tr>
                    
                    <tr>
                        <td>Gowdagere</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>1.0</td>
                        <td>1.0</td>
                    </tr>
                    
                <tr bgcolor = "#9bc4ff">
                    <td>C2Cs on New Platform</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                </tr>
            
            <tr>
                <td rowspan = 6>
                    Maharashtra
                </td>
                <td bgcolor = #fbf193>Total</td>
                <td bgcolor = #fbf193>1.0</td>
                <td bgcolor = #fbf193>8.0</td>
                <td bgcolor = #fbf193>9.0</td>
                <td bgcolor = #fbf193>73.0</td>
                <td bgcolor = #fbf193>38.0</td>
                <td bgcolor = #fbf193>111.0</td>
            </tr>
            
                    <tr>
                        <td>Jawalga</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>43.0</td>
                        <td>0</td>
                        <td>43.0</td>
                    </tr>
                    
                    <tr>
                        <td>Karad</td>
                        <td>0</td>
                        <td>3.0</td>
                        <td>3.0</td>
                        <td>0</td>
                        <td>15.0</td>
                        <td>15.0</td>
                    </tr>
                    
                    <tr>
                        <td>Killari-Karkhana</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>16.0</td>
                        <td>0</td>
                        <td>16.0</td>
                    </tr>
                    
                    <tr>
                        <td>Koregaon</td>
                        <td>0</td>
                        <td>5.0</td>
                        <td>5.0</td>
                        <td>11.0</td>
                        <td>23.0</td>
                        <td>34.0</td>
                    </tr>
                    
                <tr bgcolor = "#9bc4ff">
                    <td>C2Cs on New Platform</td>
                    <td>1.0</td>
                    <td>0</td>
                    <td>1.0</td>
                    <td>3.0</td>
                    <td>0</td>
                    <td>3.0</td>
                </tr>
            
            <tr>
                <td rowspan = 3>
                    Madhya Pradesh
                </td>
                <td bgcolor = #fbf193>Total</td>
                <td bgcolor = #fbf193>0</td>
                <td bgcolor = #fbf193>0</td>
                <td bgcolor = #fbf193>0</td>
                <td bgcolor = #fbf193>0</td>
                <td bgcolor = #fbf193>4.0</td>
                <td bgcolor = #fbf193>4.0</td>
            </tr>
            
                    <tr>
                        <td>Barkheda Bhogi</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>4.0</td>
                        <td>4.0</td>
                    </tr>
                    
                <tr bgcolor = "#9bc4ff">
                    <td>C2Cs on New Platform</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                </tr>
            
            <tr>
                <td rowspan = 7>
                    Gujarat
                </td>
                <td bgcolor = #fbf193>Total</td>
                <td bgcolor = #fbf193>10.0</td>
                <td bgcolor = #fbf193>25.0</td>
                <td bgcolor = #fbf193>35.0</td>
                <td bgcolor = #fbf193>38.0</td>
                <td bgcolor = #fbf193>56.0</td>
                <td bgcolor = #fbf193>93.0</td>
            </tr>
            
                    <tr>
                        <td>Rampur</td>
                        <td>0</td>
                        <td>9.0</td>
                        <td>9.0</td>
                        <td>0</td>
                        <td>16.0</td>
                        <td>16.0</td>
                    </tr>
                    
                    <tr>
                        <td>Navalpur</td>
                        <td>0</td>
                        <td>6.0</td>
                        <td>6.0</td>
                        <td>0</td>
                        <td>13.0</td>
                        <td>13.0</td>
                    </tr>
                    
                    <tr>
                        <td>Gandhinagar</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>4.0</td>
                        <td>4.0</td>
                    </tr>
                    
                    <tr>
                        <td>Alvakampa</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>18.0</td>
                        <td>0</td>
                        <td>18.0</td>
                    </tr>
                    
                    <tr>
                        <td>Dahegam</td>
                        <td>10.0</td>
                        <td>10.0</td>
                        <td>20.0</td>
                        <td>20.0</td>
                        <td>22.0</td>
                        <td>42.0</td>
                    </tr>
                    
                <tr bgcolor = "#9bc4ff">
                    <td>C2Cs on New Platform</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                </tr>
            
    </table>
    </body>
    </html>
    
"""
# part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# msg.attach(part1)
msg.attach(part2)
  
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.start()
server.login("neel.parmar@trringo.com", "tatwchpxogusxvtc")
server.sendmail(sender, receiver,msg.as_string())
# s.sendmail(sender, receiver, msg.as_string())
# s.quit()