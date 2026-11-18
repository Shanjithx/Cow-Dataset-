import os
import requests
from urllib.parse import urlparse

# Complete structured dataset mapping
dataset_structure = {
    "dataset for training": {
        "emaciated_cows": [
            "https://t4.ftcdn.net/jpg/11/94/42/27/360_F_1194422714_gfbaw8SIBDBH2CHCm3QqddeYSvDl0kXZ.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSAj8XrH_sR_pFpphpaJ1EDLsVOVyu-CPd2cnKrDSX33yHQf0ueUh_Fb02&s=10",
            "https://thumbs.dreamstime.com/b/skinny-brown-cow-eating-bucket-rural-farm-setting-emaciated-grazing-near-farmyard-image-portrays-life-agriculture-400274807.jpg",
            "https://images.squarespace-cdn.com/content/v1/58dbb726d1758e873aa2d72b/1539454799174-SGTQLUL2QH7BLNP84QR3/IMG_4783.JPG",
            "https://thumbs.dreamstime.com/b/skinny-brown-cow-eating-bucket-rural-farm-setting-emaciated-grazing-near-farmyard-image-portrays-life-agriculture-406594446.jpg",
            "https://www.shutterstock.com/image-photo/malnourished-skinny-hungry-cow-standing-260nw-2531578809.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_a6PaVtz2-ybdbaY-KsvwYUj4GjvWxbmc0XuKn-wrF25DeNf1rUg3WCQ&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyY1N2Dg0XMbM5bVFR5X4PJPRIBPbaZH9Wa7XDh4DO0JQ7rbspWQySJ9nF&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9dimWLM3jhdp3JO1I9DTlAJ5zpWjzwjhN-LzYFhv_f7oBFN_TdLmC_qc&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3aXbU8MmQ8jVSzerh7zk7u9EU84UC6nh0QgrprJz_hoXO-5kmDbvRO0g&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMRn9Ce7iobJnwYGvYZlKayriAWIEZ8E5FzyhiDBCn4eDT-zvRWIwpnZc&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqRM99t57ibRtHQZUpfd5rLLLQA7cbrelXiiYKvCRuRVkcZA_4MLirgBg&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSM48LkfBBLjEO5z4LD7dZOghhVGtyEhVXnEpv8F494VdQrEvZSh3VWMrZq&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmdKAj1Ny0dbuPJfYz0wupZvjSwtMZwYxwei7afrG_qv7UMb5kG86noGI&s=10",
            "https://thumbs.dreamstime.com/z/beyond-saving-care-veterinarian-sickly-weak-cow-verge-death-bokeh-dying-cow-390648262.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLvdbrSHvT6TsOUWbgYwMV41xJVuc9htERWTfcXdhUBNea7LTFOnhTt5I&s=10"
        ],
        "healthy_cows": [
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThPOdJ5hOTyJ0IJDbW8NWolGW7jCIpqdpPCLf_tWcO1efMQn2HrkU-vsA5&s=10",
            "https://images.squarespace-cdn.com/content/v1/623b572ac9761d2608d13053/397699b6-fdbb-4d28-96a5-7526b8d9ef64/Cow_female_black_white.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5V13oo6uaKQAh_ioJ9bklerFkXXtD0kH_qEyHKlaTalNNuD3ty2bgD43G&s=10",
            "https://www.shutterstock.com/image-photo/dairy-cows-walking-along-village-260nw-2652894183.jpg",
            "https://www.nadis.org.uk/media/2703/fig6.jpg",
            "https://tiimg.tistatic.com/fp/1/005/719/healthy-cattle-hf-cow-346.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZgXo5h4EpJgGokXzOIbIAMtVc1vTB_KPpiddnf5cBVQ&s=10",
            "https://futurebeef.com.au/wp-content/uploads/BCS-3.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThYqQzL_25YD6UNejtx0yeoR5lSaTEvXBo1Q8Os7tlGp5BRsqoW7xgsW3p&s=10",
            "https://www.nadis.org.uk/media/2700/fig3.jpg",
            "https://static.toiimg.com/thumb/msid-124084254,width-1280,height-720,resizemode-4/124084254.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6-AF1X-RfPh1NkbiLzEHGiuZCSHtb6Zp_l4qdHdA-cA&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_NWbA5Tbw870GX46oB7c1exY1E6c9WeJ1NCTTEGkPZBxI-HrbuBJRCVEw&s=10",
            "https://extension.psu.edu/media/catalog/product/d/3/d3a8593e95ca5722c0e09b89a286fb82.jpeg?quality=80&bg-color=255,255,255&fit=bounds&height=448&width=676&canvas=676:448",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVUaLeXa5kZDw7oTI6m1pmSjAGoevhHQu4TkS1cg8Ipaz0PHprWBj9Vyjw&s=10",
            "https://cpimg.tistatic.com/05597413/b/5/Live-Healthy-Simmental-Cattle-Cow-For-Sale.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcMFcwiKfZ6bUfJ7QdTCkfkrp1DcjCQHcuLopi8Ik-CxHwizS2dDQAeUIB&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwNHP472MbIwhekXwLhCTIwhSYd8LboCgiI3ootS2ByWCbwzP47cMU-zWo&s=10",
            "https://media.istockphoto.com/id/1213727412/photo/brown-and-white-agitated-cow-walks-by-across-a-yellow-dry-field-as-background-the-horizon.jpg?s=612x612&w=0&k=20&c=O4eHYu9z4zZj4r-476Gh6I74VeLYPTU91aRADcnCiec="
        ],
        "mastitis_udder": [
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTK-ytrp98vqPup9564i2A6pv0VA8tYOHWWbHI9noNJOUO8vMPK5D33AMN&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrf-O8z1AftqoIEquxMNAKNWWsvy2AfBg5vwqlk422aL8X66_38RLVqT3J&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgA-UcmZ__ntiP7FK1u8NgIhmdXOvrr27bcqZK2cYHE1GmutPVKSL1zhOY&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRqmomeRqKdQ0tHH06hnPmudJdMnwvSMBNUruFUqZh6sAkibJhBm591cLz&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREVPxFfTf_og8TJD6L11fbWmjwZGD3tfOOs0Ec4EvIYLxJAYb6yxSIz0M&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDgD6RxTs-Cf2XbTYAHqT4EL45t8_57WMENxcJjMkzTOaPNrkqsxseE64&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqxffKZtqsV76Dq6p70_bGpsLQI8IMXJbYm8hrDgLSuPmQ1z2VMBWxf3Q&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTb_T3WoJHgPlURHePi7UX4qRCW-n6CrDcq55S4Wo6WWb7rMso1n9stHjI&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeGHZAfw2Y2HSZ5lPxl2qsevekK9oSXFAvgbtNy-cf3wvEnyTndGx-QyQz&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ67XwVPgLXLTwYjmqqa3obX-bL4Gpi3bmmzHrxlH84cg&s=10",
            "https://tse3.mm.bing.net/th/id/OIP.1VsnVxkSZV2ZVx8GW-TloAHaEK?r=0&w=1200&h=675&rs=1&pid=ImgDetMain&o=7&rm=3",
            "https://dairybusiness.com/wp-content/uploads/2021/05/Dry-Period-Mastitis.jpg",
            "https://image.slidesharecdn.com/masititisindairycattlecausesandtratment-170513083923/85/Mastitis-in-dairy-cattle-causes-and-treatment-18-320.jpg"
        ],
        "fmd": [
            "https://upload.wikimedia.org/wikipedia/commons/e/e4/Foot_and_mouth_disease_in_mouth.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_0Wy30lOEy5Uv89SFXYwvwABL0Skcg0rETohjysQedlYmDv7rJn5GTJg&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwlRp7B6_8hhIkzLQlaFECTsQ4xIfe8f_3uO_BrtWgdFzCl_go7YkXzla6&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7KMutWhi5ahRuerBSM6QjEJDAnM7fVbY68avHOKKd0ZehQFqNsuh2Pq_W&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFlz1AXoyyXsgo7AnrUQV7LNuF0WusQnQikqXDqj_UXb1BkLGO6s6jfRWM&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkPswO5M0IsXuGtpGpi8pV9FO2NbyUFZ8UwP-mreMGes3nMMhgNn-PVOo&s=10",
            "https://www.cfsph.iastate.edu/DiseaseInfo/ImageDB/FMD/FMD_010.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnMr1xBL0fzw9HGjRheHJ-N6Duzbq-pA-LrIaDlUIOWFsfS12YtEL8LKM&s=10",
            "https://pixie.co.in/wp-content/uploads/2025/05/1x-1.webp",
            "https://agriculture.vic.gov.au/biosecurity/animal-diseases/foot-and-mouth-disease/signs-of-foot-and-mouth-disease/look-for-the-signs-of-foot-and-mouth-disease/Cattle-ruptured-mouth-blister-web.jpg",
            "https://www.infonet-biovision.org/res/res/files/3598.500x400.jpeg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeK_sgb82E1eNMpl1nWrkGS2wMVpVkp6y-Sfs9ooShB8V9WW6dG2bXU87w&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGnqrc_LU6caBY6IR0n0CyJs-iVbF_gDK1Ba8cZOtUp_6Xi50n_P2Jcgqe&s=10",
            "https://www.shutterstock.com/image-photo/foot-mouth-disease-fmd-cattle-260nw-2546120975.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWgRhyYDZdu6jRZA7z9_UeuxhAmt6oYlsgRojxIhtAIvC1b3LKe2IbDRD6&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8N4MuIMVoW6sHg3mR7nyTNGdvSOTVkPy51IretsvXMDvtn7oa0sXL7xuZ&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgm-fY5Gj2y4D_EbfEJ2M9MAU8T0LxZFI0xnudHpJyqlqBB6P2sAZwQU8&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSma5lSnnzf0iGLizvd-2lwErgT4UruZuBnMLqmQ5UIXbQn5fRCl8xovR6e&s=10"
        ],
        "lsd": [
            "https://www.nadis.org.uk/media/1302/fig-1.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQq-riiSDs-PUAeFdvgW4A7p4plfxNzpuAFUz8_6V3pej8GuQ-PdW0qiQw&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSeruy0-0dCxJ1DoDIkzOfqRAlk7yyzfynEfQ242F715kk4K0iLOmOhLA&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcHtB-B-94VWZ7gHkrmRGaQaeN08SzihNsPLV_h6py1NPZIEHlQqksnAaL&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRi-5r06AkVrSgAUAzmWzlt0JC_bDBoQUNOz5EVyHs-pVKi-MECF0KC518I&s=10",
            "https://www.farmersweekly.co.za/wp-content/uploads/2016/01/Lumpy-skin-disease-cattle.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgBTdDl4pHpPonNtQtN1lox0g_0kuEtlYEee_6qsglQGWNbJ8KMBY4OHw&s=10",
            "https://media.springernature.com/lw1200/springer-static/image/art%3A10.1007%2Fs00203-024-03932-6/MediaObjects/203_2024_3932_Fig6_HTML.jpg",
            "https://i.ex-cdn.com/nongnghiepmoitruong.vn/files/content/2025/03/12/dap-tat-benh-viem-da-noi-cuc-143215_365.jpeg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIPtgk16VGFEQJSfVmkGBfQmwpMDU1eVkOI9I0MnMYeAAXSUS_OiWVs-A&s=10",
            "https://www.nadis.org.uk/media/2300/photo-4-pb-20sep16.jpg",
            "https://etimg.etb2bimg.com/photo/94147162.cms?mod=55018",
            "https://c.files.bbci.co.uk/BB2E/production/_127281974_gettyimages-1243405341.jpg",
            "https://d14a823tufvajd.cloudfront.net/images/Sewaj237CFtNyF5leLKO.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoYo9PekzwS5oHULU2QuPPHDGSoFlceJZO--vIj2BlpQ&s=10",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0-PorHOFaPl6srKEvIVTERpihlUq0pNZWN-yXlS-_ypsyNE1ePXNX5y4&s=10",
            "https://resize.indiatvnews.com/en/resize/newbucket/1200_-/2023/08/lumpy-virus-1692266219.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh0vstmfmw3_xO2I3xJmyr747LaiHiXXwWMnTJ2p_YprM5NM2au90FSPY&s=10",
            "https://www.pharmabiz.com/NewsImages/lead5_lumpy_skin_cattle.jpg"
        ],
        "diverse_cow_breeds": [
            "https://girorganic.com/cdn/shop/articles/what-is-gir-cow-453725.jpg?v=1673547600",
            "https://upload.wikimedia.org/wikipedia/commons/3/31/Sahiwala_02_%28cropped%29.JPG",
            "https://www.dairyknowledge.in/dkp/sites/default/files/styles/medium_large/public/red_sindhi_cow.jpg?itok=Cbt6wHpV",
            "https://upload.wikimedia.org/wikipedia/commons/f/f1/Holstein-Friesian_in_Dundee%2C_Quebec.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/5/55/Bou%C3%ABts_d%27J%C3%A8rri_%C3%8Agypte_5_J%C3%A8rri_Mai_2009.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRFi7ULG3PFkDcVQPiV93RUhMIxyRoHzGZr4TP7DA-EENhofJr&s=10",
            "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcStCNagQJJms8Uun7rQcg_sYuyXte5MwZqh-MyoE4UxaOxt2APb&s=10",
            "https://upload.wikimedia.org/wikipedia/commons/e/e5/Vechur_Cow.jpg",
            "https://www.dairyknowledge.in/dkp/sites/default/files/styles/medium_large/public/ongole_cow.jpg?itok=a52Njwua",
            "https://thumb.wikimedia.org/wikipedia/commons/thumb/2/27/Kankrej_01_%28cropped%29.JPG/1280px-Kankrej_01_%28cropped%29.JPG",
            "https://breeds.okstate.edu/cattle/site-files/images/tharparkar.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/d/d2/Kangeyam_Cow_%E0%AE%95%E0%AE%BE%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AF%87%E0%AE%AF%E0%AE%ⵎ_%E0%AE%A8%E0%AE%BE%E0%AE%9F%E0%AF%81_%E0%AE%AE%E0%AE%BE%E0%AE%9F%E0%AF%81_%28cropped%29.jpg",
            "https://brcranch.com/wp-content/uploads/2024/03/BRC-Money-Dont-Jiggle-240-1024x683.jpg",
            "https://cdn.britannica.com/04/504-050-E4CD7A19/Simmental-bull.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/7/70/Hariana_02.JPG",
            "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTzFahlw6d_0_M4vzB7J76SOCGtMKcs16LzfN34yjjnznW6v2XW&s=10",
            "https://upload.wikimedia.org/wikipedia/commons/7/74/Punganur_cattle_breed_%28cropped%29.jpg",
            "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRgmKUUcn5q3Xy-LDBdPhE6NBJSkc1lLWZqIkqMxA6WbZGLhLNX&s=10"
        ]
    }
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

print("========================================")
print("     DOWNLOADING TRAINING DATASET       ")
print("========================================")

for root_folder, categories in dataset_structure.items():
    for category, urls in categories.items():
        dir_path = os.path.join(root_folder, category)
        os.makedirs(dir_path, exist_ok=True)
        
        print(f"\n[Category: {category}] ({len(urls)} links)")
        
        for idx, url in enumerate(urls, start=1):
            parsed_url = urlparse(url)
            path = parsed_url.path
            ext = os.path.splitext(path)[1].lower()
            
            if ext not in ['.jpg', '.jpeg', '.png', '.webp', '.JPG', '.JPEG', '.PNG']:
                ext = '.jpg'
                
            file_name = f"{category}_{idx:03d}{ext}"
            file_path = os.path.join(dir_path, file_name)
            
            try:
                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    print(f"  Saved: {file_name}")
                else:
                    print(f"  Skipped (HTTP {response.status_code}): {url[:40]}...")
            except Exception as e:
                print(f"  Error downloading link {idx}: {e}")

print("\n========================================")
print("Dataset build complete! Check the folder.")
print("========================================")