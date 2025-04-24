import pandas as pd
import json

def excel_to_json(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file)

    # Drop the first column if it's an ID
    if 'id' in df.columns[0].lower() or df.columns[0].lower().strip() == 'id':
        df = df.iloc[:, 1:]

    # Rename columns to expected format
    df.columns = ['title', 'meaning', 'example']

    # Combine into desired structure
    data = []
    for _, row in df.iterrows():
        title = str(row['title']).strip()
        meaning = str(row['meaning']).strip()
        example = str(row['example']).strip()

        data.append({
            "title": title,
            "description": f"{meaning}\nExample: {example}"
        })

    # Write to JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✅ JSON saved to {output_file}")

# Usage
excel_to_json("Zootechnics.xlsx", "Zootechnics.json")
excel_to_json("Neuroethology.xlsx", "Neuroethology.json")
excel_to_json("Mammalogy_Terms.xlsx", "Mammalogy_Terms.json")
excel_to_json("Herpetology_Terms.xlsx", "Herpetology_Terms.json")
excel_to_json("Embryology_topic.xlsx", "Embryology_topic.json")

excel_to_json("Ecology_dictionary.xlsx", "Ecology_dictionary.json")
excel_to_json("Applied_Zoology.xlsx", "Applied_Zoology.json")