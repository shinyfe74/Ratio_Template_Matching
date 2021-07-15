import cv2

def compare_ratio(src_img, template, ratio_list):
    optimal_maxVal = 0
    optimal_ratio = 0
    optimal_x = 0
    optimal_y = 0
    optimal_w = 0
    optimal_h = 0
    temp_h, temp_w = template.shape[:2]

    for ratio in ratio_list:
        resize_w = int(temp_w*ratio)
        resize_h = int(temp_h*ratio)

        resize_temp = cv2.resize(template, dsize=(resize_w, resize_h), interpolation=cv2.INTER_LINEAR)

        resize_matching = cv2.matchTemplate(src_img, resize_temp,cv2.TM_CCOEFF_NORMED)
        resize_minVal, resize_maxVal, resize_minLoc, resize_maxLoc = cv2.minMaxLoc(resize_matching)

        if resize_maxVal >= optimal_maxVal:
            optimal_ratio = round(ratio,7)
            optimal_maxVal = resize_maxVal
            optimal_x, optimal_y = resize_maxLoc
            optimal_w = resize_w
            optimal_h = resize_h

        else:
            pass

        # print(ratio_list.index(ratio), round(ratio,7),  resize_minVal, resize_maxVal, resize_minLoc, resize_maxLoc)

    return optimal_maxVal, optimal_ratio, optimal_x, optimal_y, optimal_w, optimal_h


def ratio_template_matching(original_src_img, original_template, result_path = None):
    src_img = cv2.cvtColor(original_src_img, cv2.COLOR_RGB2GRAY)
    template = cv2.cvtColor(original_template, cv2.COLOR_RGB2GRAY)
    dst_src_img = original_src_img

    #matching_accuracy
    matching_threshold = 0.95
    #for resize check threshold
    resize_threshold = 0
    temp_h, temp_w = template.shape[:2]
    src_h, src_w = src_img.shape[:2]

    if src_w/temp_w < src_h/temp_h:
        max_ratio = src_w/temp_w
    else:
        max_ratio = src_h/temp_h
    
    
    ratio_list_1 = []
    for i in range(int(max_ratio*10)+1):
        ratio_list_1.append(round(0.1*(i+1),2))

    optimal_maxVal, optimal_ratio, optimal_x, optimal_y, optimal_w, optimal_h = compare_ratio(src_img, template, ratio_list_1)
    prvious_ratio = optimal_ratio

    # print("첫번째자리수 비교 결과", optimal_ratio, optimal_maxVal, optimal_x, optimal_y, optimal_w, optimal_h)

    if optimal_maxVal > matching_threshold:
        pass

    else:
        ratio_list_2 = []
        for i in range(21):
            ratio_list_2.append(optimal_ratio-0.1+0.01*i)
        
        optimal_maxVal, optimal_ratio, optimal_x, optimal_y, optimal_w, optimal_h = compare_ratio(src_img, template, ratio_list_2)
        # print("소수 두번째자리수 비교 결과", optimal_ratio, optimal_maxVal, optimal_x, optimal_y, optimal_w, optimal_h)


    if prvious_ratio == optimal_ratio:
        pass

    else:
        prvious_ratio = optimal_ratio
        if optimal_maxVal > matching_threshold:
            pass

        else:
            ratio_list_3 = []
            for i in range(21):
                ratio_list_3.append(optimal_ratio-0.01+0.001*i)
            
            optimal_maxVal, optimal_ratio, optimal_x, optimal_y, optimal_w, optimal_h = compare_ratio(src_img, template, ratio_list_3)
            # print("소수 세번째자리수 비교 결과", optimal_ratio, optimal_maxVal, optimal_x, optimal_y, optimal_w, optimal_h)
             
            
    if prvious_ratio == optimal_ratio:
        pass

    else:
        prvious_ratio = optimal_ratio
        if optimal_maxVal > matching_threshold:
            pass

        else:
            ratio_list_4 = []
            for i in range(21):
                ratio_list_4.append(optimal_ratio-0.001+0.0001*i)
            
            optimal_maxVal, optimal_ratio, optimal_x, optimal_y, optimal_w, optimal_h = compare_ratio(src_img, template, ratio_list_4)
            # print("소수 네번째자리수 비교 결과", optimal_ratio, optimal_maxVal, optimal_x, optimal_y, optimal_w, optimal_h)  


    if prvious_ratio == optimal_ratio:
        pass

    else:
        prvious_ratio = optimal_ratio
        if optimal_maxVal > matching_threshold:
            pass

        else:
            ratio_list_5 = []
            for i in range(21):
                ratio_list_5.append(optimal_ratio-0.0001+0.00001*i)
            
            optimal_maxVal, optimal_ratio, optimal_x, optimal_y, optimal_w, optimal_h = compare_ratio(src_img, template, ratio_list_5)
            prvious_ratio = optimal_ratio
            # print("소수 다섯번째자리수 비교 결과", optimal_ratio, optimal_maxVal, optimal_x, optimal_y, optimal_w, optimal_h)  



    print("Matching Result", optimal_ratio, round(optimal_maxVal,7), optimal_x, optimal_y, optimal_w, optimal_h)  
    dst_src_img = cv2.rectangle(dst_src_img, (optimal_x, optimal_y),
                                (optimal_x + optimal_w, optimal_y + optimal_h), (0, 0, 255), 2)
    dst_src_img = cv2.putText(dst_src_img,"ratio: {0}, accuracy {1}".format(optimal_ratio, round(optimal_maxVal,7)),(optimal_x, optimal_y), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,0), 3)
    
    cv2.imshow("template", original_template)
    cv2.imshow("result", dst_src_img)

    
    if result_path != None:
        cv2.imwrite(result_path, dst_src_img)
    else:
        pass
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    result_list = [optimal_ratio, round(optimal_maxVal,7), optimal_x, optimal_y, optimal_w, optimal_h]
    return result_list
    
