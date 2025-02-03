import os
import pandas as pd
from openpyxl import load_workbook

# Klasör yolu tanımlaması
BASE_DIR = r"dataset_files"


def save_data_to_excel(data, filename):
    """
    Verilen dictionary listesini Excel dosyasına, önceki verileri silmeden ekler.
    Eğer dosya yoksa yeni oluşturur, varsa üzerine yeni verileri ekler.

    :param data: Liste formatında dictionary verisi
    :param filename: Kaydedilecek Excel dosyasının ismi (örn: 'team_data.xlsx')
    """
    if not data:
        print(f"UYARI: {filename} için veri bulunamadı, dosya oluşturulmadı.")
        return

    # Kaydetme yolunu oluştur
    file_path = os.path.join(BASE_DIR, filename)

    # Yeni veriyi DataFrame formatına çevir
    new_data_df = pd.DataFrame(data)

    # Eğer dosya zaten varsa, eski verileri oku ve yeni verileri ekle
    if os.path.exists(file_path):
        try:
            existing_df = pd.read_excel(file_path, engine='openpyxl')
            combined_df = pd.concat([existing_df, new_data_df], ignore_index=True)
        except Exception as e:
            print(f"Hata oluştu: {e}, dosya okunamadı. Yeni veri kaydedilecek.")
            combined_df = new_data_df
    else:
        combined_df = new_data_df

    # Güncellenmiş veriyi tekrar Excel'e yaz
    combined_df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"{filename} başarıyla güncellendi! Yol: {file_path}")
