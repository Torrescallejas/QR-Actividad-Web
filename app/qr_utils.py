import os
import qrcode

def generate_qr_code(attendee_id: int):
    output_dir = "qrcodes"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # URL de ejemplo para la validación de acceso
    url = f"http://localhost:8000/attendees/validate/{attendee_id}"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"qrcodes/attendee_{attendee_id}.png")
    
