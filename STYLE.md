# Reboot (@reboot.actu) — règles du post quotidien

Un post par jour, publié à 8 h (heure de Paris) : un carrousel Instagram sur UNE actu tech du jour, pour les 16–35 ans, en français.

## Format
- Slides 1080×1350 (4:5), JPEG.
- 6 à 8 slides : couverture → les faits → le chiffre ou le contexte → qui / pourquoi → ce qui change → « à garder en tête » (limites, qui parle, ce qu'on ne sait pas) → **dernière slide « ET TOI ? » obligatoire chaque jour** (fond orange, question liée à la news, « Dis-le en commentaire. Et abonne-toi pour le reboot de demain matin. »).
- Les fonds alternent : noir #161616, beige #E8E4D8, orange #FF5A1F (couverture = photo).

## Ce qu'on ne met JAMAIS
- Pas de petits textes en haut ou en bas : pas de date, pas de pseudo, pas de « swipe », pas de numéro de slide, pas de badge de catégorie, pas de source sur les slides (la source va dans la description).
- Pas de style terminal, néon, monospace, dégradés décoratifs, emojis sur les slides.

## Typo et couleurs
- Titres : Anton (capitales), mélangé avec Instrument Serif italique pour la partie « parlée ».
- Texte : Inter Tight 500/600, 40–46 px.
- Accent unique : orange #FF5A1F (bandeau légèrement penché -2° sur le mot ou chiffre clé). Texte clair #FFF3E2.
- Google Fonts : Anton, Instrument Serif (ital), Inter Tight.

## Couvertures (templates/) — on tourne selon la photo
- `couverture-plein-cadre.html` : photo pleine page, voile sombre en bas, gros titre.
- `couverture-detourage.html` : sujet détouré (Adobe image_remove_background) devant un énorme mot/chiffre, fond orange.
- `couverture-polaroid.html` : photo façon polaroid scotchée sur fond beige, titre Anton + serif sur bandeau orange.
La couverture = image + gros titre accrocheur, rien d'autre. Elle doit donner envie de faire défiler.

## Slides intérieures (templates/)
`slide-chiffres`, `slide-polaroid-texte`, `slide-sombre-etiquettes`, `slide-claire-liste`, `slide-sombre-points`, `slide-fin-et-toi`.

## Photos
- Vraies photos Adobe Stock, filtre `pricing: free` (licence gratuite), via le connecteur Adobe : asset_search → asset_license_and_download_stock → téléchargement.
- Jamais de logos de marques redessinés, jamais de photos de personnes réelles identifiables (célébrités) récupérées sur le web.

## Description (caption)
- 2 phrases d'accroche qui résument la news, une question pour les commentaires avec 👇, une ligne « Source : … », puis les hashtags.
- La première phrase contient les mots-clés que les gens taperaient dans la recherche Insta (ex. « IA », « ChatGPT », « iPhone », « GTA 6 ») : la recherche Instagram lit le texte de la description.
- Faits uniquement tirés de sources vérifiées le jour même ; ne rien inventer.

## Hashtags (Instagram limite à 5 par post depuis juin 2026)
Exactement 5, en minuscules, sans accents, à la fin de la description :
1. `#actutech` (toujours, c'est la signature du compte)
2. un hashtag tech FR de niche : `#techfr`, `#iafr`, `#gamingfr`, `#cybersecurite`, `#smartphonefr`… selon le sujet
3. et 4. deux hashtags précis sur le sujet du jour (le produit, la marque ou le thème : `#chatgpt`, `#gta6`, `#iphone18`, `#binance`…)
5. un hashtag d'audience : `#etudiant`, `#gamer`, `#geek`, `#nouvelletechnologie`…
Préférer les hashtags précis et moyennement utilisés aux énormes hashtags génériques (#tech, #ai) où le post est noyé.

## Reels (lundi, mercredi, vendredi)
- Motion design vertical 1080×1920, 22–28 s, SANS voix (Clément ne veut pas de voix de synthèse).
- DYNAMIQUE mais LISIBLE (retours de Clément) : 8 à 10 scènes ; une scène sans texte important peut durer 2 s, mais une scène avec une info (chiffre, phrase) reste au moins 2,5 s APRÈS que tout le texte est affiché, pour qu'on ait le temps de lire. PAS de secousses ni de coups de zoom caméra sur le temps (« ça n'apporte rien »). mélange de VRAIS EXTRAITS VIDÉO Adobe Stock (gratuits, contentType "Video", pricing "free", licence en 1080) et de photos, mots qui arrivent un par un sur le temps, titres qui « claquent » (zoom 1,6→1 avec rebond), compteurs de chiffres, flash court à chaque coupe, polaroid qui tombe.
- Au moins 3 extraits vidéo différents par Reel. Découpe-les avec ffmpeg en images JPEG 1080×1920 à 30 i/s (crop 9:16) dans un dossier clips/ et charge-les image par image (voir le modèle).
- Même charte que le carrousel : Anton + Instrument Serif italique + Inter Tight, noir / beige / orange #FF5A1F, scène finale « ET TOI ? » orange.
- Changements de scène calés sur le tempo de la musique. Zones sûres : rien d'important à moins de 250 px du haut, 350 px du bas, 120 px du bord droit.
- Musique : piste instrumentale libre d'Adobe Stock (asset_search contentType "Audio", pricing "free", puis licence). Ne JAMAIS pousser l'audio ni les extraits vidéo bruts dans ce dépôt public.
- Outils : `tools/reel/exemple-reel.html` (modèle validé : scènes, `window.render(t)` asynchrone, `window.DURATION`) et `tools/reel/capture.py` (capture image par image). Encodage ffmpeg H.264 + AAC, 30 i/s, -movflags +faststart.
- Fichiers à déposer : `reel.mp4`, `reel-cover.jpg` (image où le titre est lisible), `reel-caption.txt` (mêmes règles que la description, 5 hashtags).

## Publication
- Fichiers poussés dans `posts/AAAA-MM-JJ/` de ce dépôt public.
- Liens publics via jsDelivr (bons types MIME, indispensable pour la vidéo) : `https://cdn.jsdelivr.net/gh/CLM-HND/reboot-actu-media@<hash du commit>/posts/AAAA-MM-JJ/<fichier>`
- Publication via le connecteur Windsor.ai : instagram, create_carousel_post pour le carrousel et create_video_post pour le Reel, compte reboot.actu.
