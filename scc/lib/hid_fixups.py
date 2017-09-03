#!/usr/bin/env python2
"""
List of known HID report replacements for some controllers.
Taken mostly from Linux kernel source.
"""

# First key is vendor id, 2nd is device. Value is just HID report bytes

HID_FIXUPS = {
	0x0079: {
		0x0011 : [	# DragonRise Inc. SNES-like Gamepad
				0x05, 0x01,         #  Usage Page (Desktop)
				0x09, 0x04,         #  Usage (Joystick)
				0xA1, 0x01,         #  Collection (Application)
				0xA1, 0x02,         #      Collection (Logical)
				0x14,               #          Logical Minimum (0)
				0x75, 0x08,         #          Report Size (8)
				0x95, 0x03,         #          Report Count (3)
				0x81, 0x01,         #          Input (Constant)		# offset 0 - 24
				0x26, 0xFF, 0x00,   #          Logical Maximum (255)
				0x95, 0x02,         #          Report Count (2)
				0x09, 0x30,         #          Usage (X)
				0x09, 0x31,         #          Usage (Y)
				0x81, 0x02,         #          Input (Variable)		# offset 24, 32
				0x75, 0x01,         #          Report Size (1)
				0x95, 0x04,         #          Report Count (4)
				0x81, 0x01,         #          Input (Constant)		# offset 40 - 44
				0x25, 0x01,         #          Logical Maximum (1)
				0x95, 0x0A,         #          Report Count (10)
				0x05, 0x09,         #          Usage Page (Button)	# offset 44 - 54
				0x19, 0x01,         #          Usage Minimum (01h)
				0x29, 0x0A,         #          Usage Maximum (0Ah)
				0x81, 0x02,         #          Input (Variable)
				0x95, 0x0A,         #          Report Count (10)
				0x81, 0x01,         #          Input (Constant)
				0xC0,               #      End Collection,
				0xC0                #  End Collection
		],
	},
	0x1038: {
		0x1410 : [	# Steelseries SRW-S1 wheel controller
				0x05, 0x01, 0x09, 0x08, 0xA1, 0x01, 0xA1, 0x02, 0x95, 0x01,
				0x05, 0x01, 0x09, 0x30, 0x16, 0xF8, 0xF8, 0x26, 0x08, 0x07,
				0x65, 0x14, 0x55, 0x0F, 0x75, 0x10, 0x81, 0x02, 0x09, 0x31,
				0x15, 0x00, 0x26, 0xFF, 0x03, 0x75, 0x0C, 0x81, 0x02, 0x09,
				0x32, 0x15, 0x00, 0x26, 0xFF, 0x03, 0x75, 0x0C, 0x81, 0x02,
				0x05, 0x01, 0x09, 0x39, 0x25, 0x07, 0x35, 0x00, 0x46, 0x3B,
				0x01, 0x65, 0x14, 0x75, 0x04, 0x95, 0x01, 0x81, 0x02, 0x25,
				0x01, 0x45, 0x01, 0x65, 0x00, 0x75, 0x01, 0x95, 0x03, 0x81,
				0x01, 0x05, 0x09, 0x19, 0x01, 0x29, 0x11, 0x95, 0x11, 0x81,
				0x02, 0x05, 0x01, 0x09, 0x33, 0x75, 0x04, 0x95, 0x02, 0x15,
				0x00, 0x25, 0x0b, 0x81, 0x02, 0x09, 0x35, 0x75, 0x04, 0x95,
				0x01, 0x25, 0x03, 0x81, 0x02, 0x06, 0x00, 0xFF, 0x09, 0x01,
				0x75, 0x04, 0x95, 0x0D, 0x81, 0x02, 0xC0, 0xA1, 0x02, 0x09,
				0x02, 0x75, 0x08, 0x95, 0x10, 0x91, 0x02, 0xC0, 0xC0
		],
	},
	0x054c: {
			0x0268 : [	# Dualshock3. This one is completely imaginary,
						# generated just so hiddrv parses correct data
						# Don't use for anything but SCC.
			0x05, 0x01,         # Usage Page (Desktop),
			0x09, 0x04,         # Usage (Joystick),
			0xA1, 0x01,         # Collection (Application),
			0xA1, 0x02,         #     Collection (Logical),
			0x75, 0x08,         #         Report Size (8),
			0x95, 0x01,         #         Report Count (1),
			0x81, 0x01,         #         Input (Constant),
			0x14,               #         Logical Minimum (0),
			0x25, 0x01,         #         Logical Maximum (1),
			0x75, 0x01,         #         Report Size (1),
			0x95, 25,           #         Report Count (25),
			0x05, 0x09,         #         Usage Page (Button),
			0x81, 0x02,         #         Input (Variable),
			
			0x95, 7,            #         Report Count (7),
			0x81, 0x01,         #         Input (Constant),
			0x75, 0x08,         #         Report Size (8),
			0x95, 1,            #         Report Count (1),
			0x81, 0x01,         #         Input (Constant),
			
			0x75, 0x08,         #         Report Size (8),
			0x14,               #         Logical Minimum (0),
			0x26, 0xFF, 0x00,   #         Logical Maximum (255),
			0x95, 0x04,         #         Report Count (4),
			0x09, 0x30,         #         Usage (X),
			0x09, 0x31,         #         Usage (Y),
			0x09, 0x33,         #         Usage (RX),
			0x09, 0x34,         #         Usage (RY),
			0x81, 0x02,         #         Input (Variable),
			
			0x95, 8,            #         Report Count (8),
			0x81, 0x01,         #         Input (Constant),
			
			0x75, 0x08,         #         Report Size (8),
			0x95, 0x02,         #         Report Count (2),
			0x09, 0x30,         #         Usage (X),
			0x09, 0x31,         #         Usage (Y),
			0x81, 0x02,         #         Input (Variable),
			0x95, 0x02,         #         Report Count (4),
			0x81, 0x01,         #         Input (Constant),
			
			0x75, 0x08,         #         Report Size (8),
			0x95, 27,           #         Report Count (27),
			0x81, 0x01,         #         Input (Constant),
			0xC0,               #     End Collection,
			0xC0                # End Collection
		]
	},
}