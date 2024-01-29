def convert(feet, inches):
    result = round(float(feet) * 0.3048 + float(inches) * 0.0254, 3)
    return f"{result} m"