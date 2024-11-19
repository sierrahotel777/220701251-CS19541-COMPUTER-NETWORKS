def string_to_bits(s):
    """Convert a string to a list of bits."""
    return ''.join(format(ord(c), '08b') for c in s)

def calculate_redundant_bits(m):
    """Calculate the number of redundant bits needed."""
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r
           
def insert_redundant_bits(data_bits):
    """Insert redundant bits into the data bits."""
    m = len(data_bits)
    r = calculate_redundant_bits(m)
    encoded_bits = ['0'] * (m + r)
   
    # Insert data bits into positions that are not powers of 2
    j = 0
    for i in range(1, len(encoded_bits) + 1):
        if (i & (i - 1)) == 0:  # Check if i is a power of 2
            continue
        encoded_bits[i - 1] = data_bits[j]
        j += 1
   
    # Calculate parity bits
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for j in range(parity_pos - 1, len(encoded_bits), 2 * parity_pos):
            for k in range(parity_pos):
                if j + k < len(encoded_bits):
                    parity ^= int(encoded_bits[j + k])
        encoded_bits[parity_pos - 1] = str(parity)
   
    return ''.join(encoded_bits)

def detect_and_correct(encoded_bits):
    """Detect and correct errors in the encoded bits."""
    r = 0
    while (2 ** r) <= len(encoded_bits):
        r += 1
    error_pos = 0
   
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for j in range(parity_pos - 1, len(encoded_bits), 2 * parity_pos):
            for k in range(parity_pos):
                if j + k < len(encoded_bits):
                    parity ^= int(encoded_bits[j + k])
        if parity != 0:
            error_pos += parity_pos
   
    return error_pos

def main():
    input_str = input("Enter the string to encode: ")
    data_bits = string_to_bits(input_str)
   
    print("Original data bits: {}".format(data_bits))
   
    r = calculate_redundant_bits(len(data_bits))
    print("Number of redundant bits needed: {}".format(r))
   
    encoded_bits = insert_redundant_bits(data_bits)
    print("Encoded bits with redundant bits: {}".format(encoded_bits))
   
    # Ask user for the bit position to change
    user_input = input("Enter the bit position (1-based index) to change (or 0 to skip): ")
    if user_input != '0':
        bit_position = int(user_input) - 1  # Convert to 0-based index
        if 0 <= bit_position < len(encoded_bits):
            encoded_bits_list = list(encoded_bits)
            encoded_bits_list[bit_position] = '1' if encoded_bits_list[bit_position] == '0' else '0'
            encoded_bits = ''.join(encoded_bits_list)
            print("Bit at position {} changed. Updated encoded bits: {}".format(bit_position + 1, encoded_bits))
        else:
            print("Invalid bit position entered. No changes made.")
   
    # Detect and correct the error
    detected_error_pos = detect_and_correct(encoded_bits)
    if detected_error_pos:
        print("Detected error at position: {}".format(detected_error_pos))
        encoded_bits_list = list(encoded_bits)
        encoded_bits_list[detected_error_pos - 1] = '1' if encoded_bits_list[detected_error_pos - 1] == '0' else '0'
        encoded_bits = ''.join(encoded_bits_list)
        print("Corrected encoded bits: {}".format(encoded_bits))
    else:
        print("No errors detected.")
   
    # Extract data bits from corrected encoded bits
    corrected_data_bits = [encoded_bits[i] for i in range(len(encoded_bits)) if (i + 1) & (i) != 0]
    corrected_data_bits = ''.join(corrected_data_bits)
   
    print("Corrected data bits: {}".format(corrected_data_bits))
    original_message = ''.join(chr(int(corrected_data_bits[i:i + 8], 2)) for i in range(0, len(corrected_data_bits), 8))
    print("Original message: {}".format(original_message))

if __name__ == "__main__":
    main()