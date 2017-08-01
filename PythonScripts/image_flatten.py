from pyExplorer.rawDataExplorer import imageprint

printer = imageprint.ImagePrinter('W:\\2015_09_HTS_LE\\Code_LE\Global_config\\basicSettingsLocal.py')
levelsets = [(40, 1000), (40, 1000), (40, 1000), (40, 1000)]  # between 0 and 4095 for 2x2 binned image
color_order = ["B", "G", "R", "W"]  # Tell colors for channels in the same order.
# Only options: R for red, G for green, B for blue and W for white

plateNames = ['LE_20170209_nikon210X_plate_2017018105_t48']
wells =['D6',
        'D5',
        'C9',
        'F10',
        'C7',
        'O7',
        'E4',
        'G4',
        'O5',
        'M7',
        'H10',
        'G7',
        'A7',
        'K4',
        'M14',
        'K15',
        'C3',
        'D15',
        'E12',
        'M18',
        'J21',
        'D10',
        'E5',
        'L20',
        'D19',
        'L18',
        'N9',
        'G13',
        'E3',
        'P8',
        'A5',
        'K5',
        'C16',
        'E11',
        'F5',
        'F9',
        'P4',
        'C5',
        'I14',
        'I12',
        'E10',
        'B7',
        'D9',
        'A8',
        'F8',
        'O14',
        'N13',
        'E8',
        'B6',
        'E18',
        'B8',
        'K21',
        'C4',
        'O21',
        'D11',
        'E6',
        'C22',
        'F7',
        'B4',
        'D8',
        'F6',
        'H3',
        'D4',
        'D3',
        'M21',
        'B3',
        'G9',
        'I13',
        'C6',
        'J6',
        'D7',
        'P7',
        'O11']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=500)


plateNames = ['LE_20170209_nikon210X_plate_2017018104_t48']
wells= ['F19',
        'D8',
        'D14',
        'K13',
        'K21',
        'N3',
        'I3',
        'O12',
        'K3',
        'I21',
        'C5',
        'A16',
        'K5',
        'C13',
        'C7',
        'E7',
        'C3',
        'H9',
        'M9',
        'A14',
        'A13',
        'E4',
        'M4',
        'D9',
        'A6',
        'L16',
        'M21',
        'G8',
        'N16',
        'P5',
        'K19',
        'B18',
        'E8',
        'A10',
        'L18',
        'A11',
        'C11',
        'A21',
        'B4',
        'G16',
        'K22',
        'H13',
        'J13',
        'O18',
        'D17',
        'B3',
        'D15',
        'J3',
        'A22',
        'M18',
        'I22',
        'A18',
        'A20',
        'K11',
        'E3',
        'E18',
        'O3',
        'G5',
        'I5',
        'H8',
        'M12',
        'C14',
        'M14',
        'E20',
        'B5',
        'E14',
        'O22',
        'D7',
        'L4',
        'J15',
        'F3',
        'D13',
        'C17',
        'G11',
        'C19',
        'G4',
        'I17',
        'A7',
        'E19',
        'K9',
        'O9',
        'M6',
        'O6',
        'O10',
        'M13',
        'G14',
        'E11',
        'K10',
        'C6',
        'M8',
        'G15',
        'L9',
        'K7',
        'A5',
        'D22',
        'O19',
        'C12',
        'I8',
        'B15',
        'K8',
        'N5',
        'F5',
        'B6',
        'C22',
        'P16',
        'J10',
        'B10',
        'D10',
        'D12',
        'F17',
        'H20',
        'H16',
        'B19',
        'F21',
        'E6',
        'B20',
        'J16',
        'D16',
        'F16',
        'E17',
        'O11',
        'I19',
        'G3',
        'G10',
        'B21',
        'D6',
        'E16',
        'I4',
        'G17',
        'G7',
        'K17',
        'D4',
        'D11',
        'K4',
        'H22',
        'D5',
        'P18',
        'A3',
        'P9',
        'B11',
        'C4',
        'E13',
        'E21',
        'K15',
        'G21',
        'M7',
        'I20',
        'O7',
        'E5',
        'H21',
        'I9',
        'C15']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=500)

#  2017018089
plateNames = ['LE_20170211_nikon210X_plate_2017018089_t48']
wells =['F5',
        'K13',
        'E12',
        'I4',
        'A6',
        'K9',
        'K10',
        'E4',
        'K15',
        'M12',
        'K4',
        'A19',
        'A4',
        'C4',
        'M9',
        'B4',
        'B9',
        'C12',
        'E5',
        'I7',
        'P9',
        'M19',
        'G12',
        'K6',
        'I10',
        'P21',
        'C8',
        'O8',
        'E7',
        'O16',
        'M11',
        'H11',
        'I16',
        'D9',
        'D7',
        'G7',
        'O9',
        'K17',
        'O5',
        'I11',
        'K19',
        'F9',
        'E3',
        'O4',
        'P7',
        'M10',
        'C7',
        'O10',
        'M17',
        'E21',
        'I3',
        'B11',
        'M7',
        'M14',
        'C22',
        'K8',
        'O17',
        'J19',
        'O3',
        'D5',
        'L4',
        'B3',
        'D3',
        'M16',
        'G9',
        'G20',
        'B15',
        'F21',
        'G13',
        'L9',
        'A22',
        'E19',
        'G17',
        'E10',
        'E6',
        'K12',
        'E8']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=500)

#  2017018086
plateNames = ['LE_20170211_nikon210X_plate_2017018086_t48']
wells =['G3',
        'F9',
        'J19',
        'F17',
        'H8',
        'B10',
        'H11',
        'N22',
        'D15',
        'L9',
        'J14',
        'P9',
        'F11',
        'N9',
        'N11',
        'D6',
        'L5',
        'E7',
        'H20',
        'N6',
        'H15',
        'D10',
        'L14',
        'B18',
        'F13',
        'N19',
        'F12',
        'N8',
        'B4',
        'J7',
        'P8',
        'L4',
        'D14',
        'F10',
        'O13',
        'H18',
        'D12',
        'P16',
        'J21',
        'L3',
        'F6',
        'J15',
        'H21',
        'P14',
        'D17',
        'B8',
        'D11',
        'B13',
        'N10',
        'F18',
        'J9',
        'L16',
        'N12',
        'H22',
        'N5',
        'C11',
        'O11',
        'D22',
        'O12',
        'G12',
        'O4',
        'E6',
        'C12',
        'I4',
        'I12',
        'A22',
        'G22',
        'A8',
        'E12',
        'B17',
        'O10',
        'O14',
        'I15',
        'I10',
        'C15',
        'O15',
        'A15',
        'N20',
        'I18',
        'E5',
        'C10',
        'C4',
        'K7',
        'L21',
        'D20',
        'E8',
        'J5',
        'I5',
        'E9',
        'J11',
        'L13',
        'J6',
        'F8',
        'N13',
        'H3',
        'P18',
        'H17',
        'D13',
        'P4',
        'B12',
        'J13'
        'B16',
        'P20',
        'N21',
        'P12',
        'B14',
        'A13',
        'B15',
        'H10',
        'F7',
        'D18',
        'H4',
        'C13',
        'P13',
        'P11']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=500)

#  2017018081
plateNames = ['LE_20170210_nikon210X_plate_2017018081_t48']
wells =['B17',
        'H19',
        'A13',
        'L19',
        'G9',
        'E15',
        'M13',
        'K9',
        'G19',
        'K13',
        'O11',
        'C21',
        'E17',
        'C13',
        'I13',
        'I7',
        'G15',
        'B16',
        'J19',
        'L16',
        'F19',
        'M21',
        'C11',
        'D20',
        'O15',
        'I17',
        'E8',
        'I11',
        'E7',
        'O17',
        'B21',
        'F11',
        'E4',
        'M4',
        'E6',
        'I6',
        'D11',
        'J8',
        'B20',
        'K8',
        'P3',
        'I3',
        'F5',
        'B19',
        'D19',
        'O10',
        'N19',
        'C9',
        'E9',
        'H20',
        'L21',
        'N21',
        'C16',
        'D7',
        'C18',
        'G18',
        'A20',
        'C20',
        'E20',
        'G20',
        'M20',
        'E22',
        'K22',
        'F18',
        'K11',
        'M11',
        'K19',
        'D21',
        'D8',
        'B18',
        'J9',
        'K18',
        'K21',
        'C19',
        'G17',
        'E21']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=500)

#  2017018079
plateNames = ['LE_20170210_nikon210X_plate_2017018079_t48']
wells =['G9',
        'M4',
        'C17',
        'G12',
        'A21',
        'O5',
        'M3',
        'G22',
        'A17',
        'E11',
        'B5',
        'G3',
        'G16',
        'P5',
        'I14',
        'I21',
        'H13',
        'K8',
        'A19',
        'C21',
        'E3',
        'E13',
        'C6',
        'M11',
        'K21',
        'O3',
        'G6',
        'E21',
        'L7',
        'M21',
        'K13',
        'O17',
        'H5',
        'G7',
        'M19',
        'K19',
        'J11',
        'A10',
        'L5',
        'C4',
        'I8',
        'P7',
        'M5',
        'B19',
        'N11',
        'J4',
        'C16',
        'G4',
        'G8',
        'E15',
        'A5',
        'I17',
        'G13',
        'K7',
        'I7',
        'I13',
        'C15',
        'G21',
        'C12',
        'C19',
        'G11',
        'O6',
        'P11',
        'E12',
        'B20',
        'L9',
        'J9',
        'H3',
        'O16',
        'F3',
        'B6',
        'G19',
        'N3',
        'B18',
        'B17',
        'C20',
        'G5',
        'M8',
        'D20',
        'H20',
        'P3',
        'K20',
        'A3',
        'E9',
        'F9',
        'N15',
        'A11',
        'C7',
        'O18',
        'M14',
        'A7',
        'O15',
        'C14',
        'I15',
        'M7',
        'G14',
        'K3',
        'O21',
        'C5',
        'C18',
        'A16',
        'M13',
        'C9',
        'E4']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=500)
