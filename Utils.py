from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('6870465A414B4E72544B69374B6B43544877486C38514E68446A39305045313176726938526544383247733D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'{code} کد تایید شما '
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)