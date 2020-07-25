# Funcaoo para criacao de texto aleatorio de tamanho parametrizado

def create_random_text(symbols, text_size=5):

    s_text = '';
    for i in range(text_size):

        # Adiciona simbolo escolhido aleatoriamente ao texto
        s_text = s_text + random.choice(symbols);

    return s_text;
    
# Funcao para criacao de imagem captcha com texto parametrizado

def create_image_captcha(captcha_text, captcha_dir="images", plot_image=False):
    
    image_captcha = ImageCaptcha();
    image = image_captcha.generate_image(captcha_text);
    
    # Salva imagem captcha
    if(not plot_image):
        image_file = captcha_dir + "/" + captcha_text + ".png"
        image_captcha.write(captcha_text, image_file)

    # Mostra imagem
    if(plot_image):
        fig = plt.figure()
        plt.imshow(image.copy());
        plt.axis('off')
        plt.show()

# Visualizacao de uma imagem gerada

captcha_text = create_random_text(symbols)
create_image_captcha(captcha_text, plot_image = True)