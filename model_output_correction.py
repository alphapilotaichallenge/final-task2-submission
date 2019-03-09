import missing_corners

ordered_corner_keys = ["UL", "UR", "LR", "LL"]

def bad_xy_to_good_xy(model_output):
    model_corrected = model_output
    
    xs = model_output[:8:2]
    ys = model_output[1:8:2]
    
    num_missing = sum([1 if x == 0 and y == 0 else 0 for x, y in zip(xs, ys)])

    # If all corners classified, check classifications are accurate
    if num_missing == 0:
        midpoint_x = sum(xs)/4.
        midpoint_y = sum(ys)/4.
        
        corners_fixed = dict()
        
        for x, y in zip(xs, ys):
            if x <= midpoint_x and y <= midpoint_y and not "UL" in corners_fixed:
                corners_fixed["UL"] = [x, y]
            elif x > midpoint_x and y <= midpoint_y and not "UR" in corners_fixed:
                corners_fixed["UR"] = [x, y]
            elif x > midpoint_x and y > midpoint_y and not "LR" in corners_fixed:
                corners_fixed["LR"] = [x, y]
            elif x <= midpoint_x and y > midpoint_y and not "LL" in corners_fixed:
                corners_fixed["LL"] = [x, y]

        num_missing = 4 - len(corners_fixed)
        model_corrected = []
        for corner_key in ordered_corner_keys:
            if corner_key in corners_fixed:
                model_corrected.extend(corners_fixed[corner_key])
            else:
                model_corrected.extend([0, 0])

    # If any corners are missing, call missing_corners algorithm
    if num_missing > 0:
        if num_missing <= 2:
            model_corrected = missing_corners.calculate_missing_corners(model_output)
        else:
            model_corrected = []
    
    return model_corrected
