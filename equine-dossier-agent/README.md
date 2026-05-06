# Equine Dossier Agent

An AI assistant to help manage horse records via WhatsApp.

## Project Structure
- `/dossiers`: Markdown files containing CVs, family trees, and awards for each horse.
- `/media`: Folder for storing photos sent via WhatsApp, organized by horse.
- `/reference_images`: Key photos used by the AI to identify individual horses.
- `processor.py`: The logic for identifying horses and filing information.

## Workflow
1. User sends a photo via WhatsApp.
2. AI uses `vision_analyze` against `reference_images`.
3. AI files the image in `/media/{horse_name}/`.
4. AI updates the corresponding file in `/dossiers/{horse_name}.md` if text info is provided.
