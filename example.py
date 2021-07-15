import matching_crop as mc
import os
import cv2

dir_path = os.path.join("./img/")

src_img = cv2.imread(dir_path+'src.jpg')

template = cv2.imread(dir_path+'template.jpg')

result_path = os.path.join("./img/result.jpg")

#if you want save the result, add "result_path"
#'ratio_template_matching' will return "Matching Result = [crop_ratio, accruray, template x, template y, template width, template height]
mc.ratio_template_matching(src_img, template, result_path)

print(mc.ratio_template_matching(src_img, template, result_path))


