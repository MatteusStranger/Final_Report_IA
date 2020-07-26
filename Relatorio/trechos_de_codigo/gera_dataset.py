# Geracao de Dataset
#
num_imagens = 1000
images_dir = "images/dataset_" + str(datetime.now())
os.mkdir(images_dir)

for i in range(num_imagens):
    captcha_text = create_random_text(symbols)
    create_image_captcha(captcha_text, captcha_dir = images_dir)