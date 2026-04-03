import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""
    
    # Duyệt qua từng pixel để lấy bit cuối cùng của 3 kênh màu (RGB)
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            
            for color_channel in range(3):
                # Lấy bit cuối cùng của giá trị màu và nối vào chuỗi nhị phân
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Chuyển đổi chuỗi nhị phân thành ký tự (mỗi 8 bit là 1 ký tự)
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        char = chr(int(byte, 2))
        
        # Dừng lại khi gặp ký tự kết thúc (trong code mẫu là '\0' hoặc 
        # khớp với dấu hiệu kết thúc ở file encrypt)
        # Lưu ý: Code trong ảnh dùng '\0', nhưng ở file encrypt trước đó dùng '1111111111111110'
        # Bạn có thể cần điều chỉnh điều kiện dừng nếu thông báo bị thừa ký tự rác.
        if char == '\0': 
            break
        message += char
        
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()