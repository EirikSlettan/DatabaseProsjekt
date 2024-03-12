from insert_into import*



forestillingsdato_kongsemne = ["2024-02-01", "2024-02-02", "2024-02-03", "2024-02-05", "2024-02-06"]
forestillingsdato_størst_av_alt_er_kjaerligheten = ["2024-02-03", "2024-02-06", "2024-02-07", "2024-02-12", "2024-02-13", "2024-02-14"]

forestillingstid_kongsemne = "19:00:00" 
forestillingstid_størst_av_alt_er_kjaerligheten = "18:30:00" 

forestillingsnavn_kongsemne = "Kongsemne"
forestillingsnavn_storst_av_alt_er_kjaerligheten = "Storst av alt er kjaerligheten"




for element in forestillingsdato_kongsemne:

    forestilling = (f"({element}, {forestillingstid_kongsemne}, {forestillingsnavn_kongsemne})") #FORESTILLING!!
    forestilling = forestilling.replace("(", "").replace(")", "").strip().split(",")
    insert_into_table("forestilling", forestilling)


for element in forestillingsnavn_storst_av_alt_er_kjaerligheten:

    forestilling = (f"({element}, {forestillingstid_størst_av_alt_er_kjaerligheten}, {forestillingsnavn_storst_av_alt_er_kjaerligheten})") #FORESTILLING!!
    forestilling = forestilling.replace("(", "").replace(")", "").strip().split(",")
    insert_into_table("forestilling", forestilling)





    

    teaterstykke = (f"({foresi},{forfatter},{sesong})") #teaterstykke
    teaterstykke = teaterstykke.replace("(", "").replace(")", "").strip().split(",")
    insert_into_table("teaterstykke", teaterstykke) #det er kun ett teaterstykke her





forestilling = (f"({forestillingsdato}, {forestillingstid}, {stykkenavn})") #FORESTILLING!!
    forestilling = forestilling.replace("(", "").replace(")", "").strip().split(",")
    insert_into_table("forestilling", forestilling)


    teaterstykke = (f"({stykkenavn},{forfatter},{sesong})") #teaterstykke
    teaterstykke = teaterstykke.replace("(", "").replace(")", "").strip().split(",")
    insert_into_table("teaterstykke", teaterstykke) #det er kun ett teaterstykke her

