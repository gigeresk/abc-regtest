import argparse


def blif_full_adder(index, a, b, cin, sum_out, cout):
    """Generate BLIF .names blocks for a 1-bit full adder"""
    result = []

    # XOR for sum: sum = a ^ b ^ cin
    result.append(f".names {a} {b} t1_{index}")
    result.append("01 1")
    result.append("10 1")

    result.append(f".names t1_{index} {cin} {sum_out}")
    result.append("01 1")
    result.append("10 1")

    # Carry out: cout = majority(a, b, cin)
    result.append(f".names {a} {b} {cin} {cout}")
    result.append("11- 1")
    result.append("1-1 1")
    result.append("-11 1")

    return "\n".join(result)


def generate_nbit_adder_blif(n: int):
    lines = []
    lines.append(".model addern")

    # Define primary inputs and outputs
    a_signals = [f"a{i}" for i in range(n)]
    b_signals = [f"b{i}" for i in range(n)]
    sum_signals = [f"sum{i}" for i in range(n)]
    carry_signals = [
        f"carry{i}" for i in range(n + 1)
    ]  # carry0 is initial carry-in (0)

    lines.append(".inputs " + " ".join(a_signals + b_signals))
    lines.append(".outputs " + " ".join(sum_signals))

    # Initial carry-in
    lines.append(".names carry0")

    # Generate full adder logic for each bit
    for i in range(n):
        adder_logic = blif_full_adder(
            index=i,
            a=a_signals[i],
            b=b_signals[i],
            cin=carry_signals[i],
            sum_out=sum_signals[i],
            cout=carry_signals[i + 1],
        )
        lines.append(adder_logic)

    lines.append(".end")
    return "\n".join(lines)


parser = argparse.ArgumentParser(description="Echo a single argument.")
parser.add_argument("width", help="Width of adder e.g. '64'")
args = parser.parse_args()

# Generate the BLIF and print or save
blif_text = generate_nbit_adder_blif(int(args.width))
print(blif_text)
