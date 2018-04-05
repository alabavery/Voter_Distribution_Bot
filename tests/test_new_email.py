import unittest.mock
from modules import new_email


class NewEmail__extract_sender(unittest.TestCase):
	"""
	def extract_sender(self):
        headers = self.raw['payload']['headers']
        return_path = [header for header in headers if header['name'].lower() == 'return-path']
        if return_path:
            sender = return_path[0]['value']
        else:
            sender = [header for header in headers if header['name'].lower() == 'from'][0]['value']

        sender = self.find_email_substring(sender)
        if sender:
            return utils.reformat_email_address(sender)
        else:
            return None
	"""
	def setUp(self):


	def test_b(self):
		n = new_email.NewEmail()



#
# class NewEmail__extract_sender(unittest.TestCase):
#
# 	def setUp(self):
# 		self.mock_raw = { 'historyId': '55081',
# 			  'id': '1609e165febd9f71',
# 			  'internalDate': '1514480748000',
# 			  'labelIds': ['UNREAD', 'IMPORTANT', 'CATEGORY_PERSONAL', 'INBOX'],
# 			  'payload': { 'body': {'size': 0},
# 			               'filename': '',
# 			               'headers': [ { 'name': 'Delivered-To',
# 			                              'value': 'tellonklein@gmail.com'},
# 			                            { 'name': 'Received',
# 			                              'value': 'by 10.25.190.213 with SMTP id '
# 			                                       'o204csp1780208lff;        Thu, 28 Dec '
# 			                                       '2017 09:05:54 -0800 (PST)'},
# 			                            { 'name': 'X-Google-Smtp-Source',
# 			                              'value': '...'},
# 			                            { 'name': 'X-Received',
# 			                              'value': 'by 10.55.125.133 with SMTP id '
# 			                                       'y127mr40089453qkc.277.1514480754622;        '
# 			                                       'Thu, 28 Dec 2017 09:05:54 -0800 (PST)'},
# 			                            { 'name': 'ARC-Seal',
# 			                              'value': '...'},
# 			                            { 'name': 'ARC-Message-Signature',
# 			                              'value': '...'},
# 			                            { 'name': 'ARC-Authentication-Results',
# 			                              'value': 'i=1; mx.google.com;       dkim=pass '
# 			                                       'header.i=@yahoo.com header.tests=s2048 '
# 			                                       'header.b=AzRltT9S;       spf=pass '
# 			                                       '(google.com: domain of '
# 			                                       'brooklynzoe@yahoo.com designates '
# 			                                       '74.6.135.124 as permitted sender) '
# 			                                       'smtp.mailfrom=brooklynzoe@yahoo.com;       '
# 			                                       'dmarc=pass (p=REJECT sp=REJECT '
# 			                                       'dis=NONE) header.from=yahoo.com'},
# 			                            { 'name': 'Return-Path',
# 			                              'value': '<brooklynzoe@yahoo.com>'},
# 			                            { 'name': 'Received',
# 			                              'value': 'from '
# 			                                       'sonic310-14.consmr.mail.bf2.yahoo.com '
# 			                                       '(sonic310-14.consmr.mail.bf2.yahoo.com. '
# 			                                       '[74.6.135.124])        by '
# 			                                       'mx.google.com with ESMTPS id '
# 			                                       '126si7246449qkg.368.2017.12.28.09.05.53        '
# 			                                       'for <tellonklein@gmail.com>        '
# 			                                       '(version=TLS1_2 '
# 			                                       'cipher=ECDHE-RSA-AES128-GCM-SHA256 '
# 			                                       'bits=128/128);        Thu, 28 Dec 2017 '
# 			                                       '09:05:54 -0800 (PST)'},
# 			                            { 'name': 'Received-SPF',
# 			                              'value': 'pass (google.com: domain of '
# 			                                       'brooklynzoe@yahoo.com designates '
# 			                                       '74.6.135.124 as permitted sender) '
# 			                                       'client-ip=74.6.135.124;'},
# 			                            { 'name': 'Authentication-Results',
# 			                              'value': 'mx.google.com;       dkim=pass '
# 			                                       'header.i=@yahoo.com header.tests=s2048 '
# 			                                       'header.b=AzRltT9S;       spf=pass '
# 			                                       '(google.com: domain of '
# 			                                       'brooklynzoe@yahoo.com designates '
# 			                                       '74.6.135.124 as permitted sender) '
# 			                                       'smtp.mailfrom=brooklynzoe@yahoo.com;       '
# 			                                       'dmarc=pass (p=REJECT sp=REJECT '
# 			                                       'dis=NONE) header.from=yahoo.com'},
# 			                            { 'name': 'DKIM-Signature',
# 			                              'value': 'v=1; a=rsa-sha256; c=relaxed/relaxed; '
# 			                                       'd=yahoo.com; tests=s2048; t=1514480752; '
# 			                                       'bh=ReOn8c/tCzXj6EJkpyEz8ql4wzKpkrubs7IarhmV9oc=; '
# 			                                       'h=From:Date:Subject:References:In-Reply-To:To:From:Subject; '
# 			                                       '...'},
# 			                            { 'name': 'X-YMail-OSG',
# 			                              'value': '...'},
# 			                            { 'name': 'Received',
# 			                              'value': 'from sonic.gate.mail.ne1.yahoo.com by '
# 			                                       'sonic310.consmr.mail.bf2.yahoo.com '
# 			                                       'with HTTP; Thu, 28 Dec 2017 17:05:52 '
# 			                                       '+0000'},
# 			                            { 'name': 'Received',
# 			                              'value': 'from '
# 			                                       'smtpgate105.mob.mail.bf1.yahoo.com '
# 			                                       '(EHLO [192.168.1.250]) '
# 			                                       '([72.30.28.47])          by '
# 			                                       'smtp408.mail.bf1.yahoo.com (JAMES SMTP '
# 			                                       'Server ) with ESMTPA ID '
# 			                                       'b52fe83da41844f54ef4009fae92cbb6          '
# 			                                       'for <tellonklein@gmail.com>;          '
# 			                                       'Thu, 28 Dec 2017 17:05:48 +0000 (UTC)'},
# 			                            { 'name': 'From',
# 			                              'value': 'Zoe Gaby <brooklynzoe@yahoo.com>'},
# 			                            { 'name': 'Content-Type',
# 			                              'value': 'multipart/alternative; '
# 			                                       'boundary=Apple-Mail-7C9CEF98-8AAC-41EC-BBC9-610C1F734AF0'},
# 			                            { 'name': 'Content-Transfer-Encoding',
# 			                              'value': '7bit'},
# 			                            {'name': 'Mime-Version', 'value': '1.0 (1.0)'},
# 			                            { 'name': 'Date',
# 			                              'value': 'Thu, 28 Dec 2017 12:05:48 -0500'},
# 			                            { 'name': 'Subject',
# 			                              'value': 'Re: TBNY Mission Dispatch'},
# 			                            { 'name': 'Message-Id',
# 			                              'value': '<E8A0273E-BD75-4E13-9ECA-02A505F2491F@yahoo.com>'},
# 			                            { 'name': 'References',
# 			                              'value': '<CALdYYTfAvDVqQ0BvtTxp6E2nYnBALV-PA_Qjc9eczApYSNjPKw@mail.gmail.com> '
# 			                                       '<2185E268-2A77-4519-BDD1-6F24E5D8B09B@yahoo.com> '
# 			                                       '<CALdYYTdiMJUTAS3phMJOs9mSnc5E=iZrENqgfCyyp-b6K2dHYw@mail.gmail.com> '
# 			                                       '<ADCB8A6B-8389-46A3-8E45-FF4250C69188@yahoo.com> '
# 			                                       '<CALdYYTdq7QBY7oy2RXvf2LDjftt-+mR-Hctyxg==-=_nvFG2WQ@mail.gmail.com> '
# 			                                       '<BFA0D946-7CE3-45C9-8C48-B5DF8B5E5B13@yahoo.com> '
# 			                                       '<CALdYYTf+kZXoBosXrizbZUN+2cXusBOJzkEF2JXW=kc3Fn8AJA@mail.gmail.com>'},
# 			                            { 'name': 'In-Reply-To',
# 			                              'value': '<CALdYYTf+kZXoBosXrizbZUN+2cXusBOJzkEF2JXW=kc3Fn8AJA@mail.gmail.com>'},
# 			                            { 'name': 'To',
# 			                              'value': 'True BlueNY <tellonklein@gmail.com>'},
# 			                            { 'name': 'X-Mailer',
# 			                              'value': 'iPhone Mail (15C153)'}],
# 			               'mimeType': 'multipart/alternative',
# 			               'partId': '',
# 			               'parts': [ { 'body': { 'data': '...',
# 			                                      'size': 11328},
# 			                            'filename': '',
# 			                            'headers': [ { 'name': 'Content-Type',
# 			                                           'value': 'text/plain; '
# 			                                                    'charset=us-ascii'},
# 			                                         { 'name': 'Content-Transfer-Encoding',
# 			                                           'value': 'quoted-printable'}],
# 			                            'mimeType': 'text/plain',
# 			                            'partId': '0'},
# 			                          { 'body': {'size': 0},
# 			                            'filename': '',
# 			                            'headers': [ { 'name': 'Content-Type',
# 			                                           'value': 'multipart/related; '
# 			                                                    'type="text/html"; '
# 			                                                    'boundary=Apple-Mail-8A366F89-DAEC-4283-900E-58A0BA092652'},
# 			                                         { 'name': 'Content-Transfer-Encoding',
# 			                                           'value': '7bit'}],
# 			                            'mimeType': 'multipart/related',
# 			                            'partId': '1',
# 			                            'parts': [ { 'body': { 'data': '...',
# 			                                                   'size': 27594},
# 			                                         'filename': '',
# 			                                         'headers': [ { 'name': 'Content-Type',
# 			                                                        'value': 'text/html; '
# 			                                                                 'charset=us-ascii'},
# 			                                                      { 'name': 'Content-Transfer-Encoding',
# 			                                                        'value': 'quoted-printable'}],
# 			                                         'mimeType': 'text/html',
# 			                                         'partId': '1.0'},
# 			                                       { 'body': { 'attachmentId': '...',
# 			                                                   'size': 2747982},
# 			                                         'filename': 'image1.jpeg',
# 			                                         'headers': [ { 'name': 'Content-Type',
# 			                                                        'value': 'image/jpeg; '
# 			                                                                 'name=image1.jpeg; '
# 			                                                                 'x-apple-part-url=484173F2-67A5-440A-87D4-543C9633C342'},
# 			                                                      { 'name': 'Content-Disposition',
# 			                                                        'value': 'inline; '
# 			                                                                 'filename=image1.jpeg'},
# 			                                                      { 'name': 'Content-Transfer-Encoding',
# 			                                                        'value': 'base64'},
# 			                                                      { 'name': 'Content-Id',
# 			                                                        'value': '<484173F2-67A5-440A-87D4-543C9633C342>'}],
# 			                                         'mimeType': 'image/jpeg',
# 			                                         'partId': '1.1'}]}]},
# 			  'sizeEstimate': 3807652,
# 			  'snippet': 'Here are the 40 from today. If you send me 40 more, it may take '
# 			             '2 weeks to do them (but maybe not) because we have a guest '
# 			             'speaker and another resistance activity for January 4. Thanks, '
# 			             'Zoe Sent from',
# 			  'threadId': '160336afe5628701'
# 		}
#
# 	def test_basic(self):
# 		# not sure whether or not this is actually basic case?
# 		found = NewEmail(self.mock_raw, None).sender
# 		expected = 'brooklynzoe@yahoo.com'
# 		self.assertEqual(found, expected)
#
#
# # class NewEmail__extract_attach(unittest.TestCase):
# # 	pass
#
#
# # class NewEmail__extract_is_from_google(unittest.TestCase):
# # 	pass
#
#
# # class NewEmail__extract_text(unittest.TestCase):
# # 	pass
#
#
# # class NewEmail__extract_is_surrender(unittest.TestCase):
# # 	pass
#
#
# # class NewEmail__extract_is_asks_for_more(unittest.TestCase):
# # 	pass