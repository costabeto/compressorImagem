#Reduz imagem para 500kb

import os
from tkinter import Tk, filedialog, messagebox
from PIL import Image

def reduzir_para_tamanho(input_path, tamanho_alvo_kb=450):
    img = Image.open(input_path)

    # 🔥 Se tiver transparência (RGBA, P), converte e aplica fundo branco
    if img.mode in ("RGBA", "P"):
        fundo = Image.new("RGB", img.size, (255, 255, 255))  # fundo branco
        if img.mode == "RGBA":
            fundo.paste(img, mask=img.split()[3])  # usa o canal alfa
        else:
            fundo.paste(img)
        img = fundo
    else:
        img = img.convert("RGB")

    qualidade = 95
    nome, ext = os.path.splitext(input_path)
    output_path = f"{nome}_450kb.jpg"

    while qualidade > 5:
        img.save(output_path, format="JPEG", quality=qualidade, optimize=True)
        tamanho_atual_kb = os.path.getsize(output_path) / 1024

        if tamanho_atual_kb <= tamanho_alvo_kb:
            messagebox.showinfo(
                "Sucesso ✅",
                f"Arquivo salvo:\n{output_path}\n\nTamanho: {tamanho_atual_kb:.2f} KB\nQualidade: {qualidade}"
            )
            return

        qualidade -= 5

    messagebox.showwarning(
        "Aviso ⚠️",
        "Não foi possível reduzir até o alvo sem perder muita qualidade."
    )

def escolher_arquivo():
    Tk().withdraw()
    caminho = filedialog.askopenfilename(
        title="Selecione a imagem",
        filetypes=[("Imagens", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")]
    )
    if caminho:
        reduzir_para_tamanho(caminho, 450)

if __name__ == "__main__":
    escolher_arquivo()
