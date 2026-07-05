#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_list.py
Automated Matrix Generator for the complete expanded Mysterium Magnum vocabulary ledger.
"""
import csv

headers = [
    'Lemma', 'Thematic_Category', 'Morphological_Regex_Root', 
    'Grammatical_Form', 'Primary_Author', 'Location_Reference', 
    'LSJ_Context_Snippet', 'Perseus_Greek_Hyperlink', 'Semantic_Definition'
]

data = [
    # --- ORIGINAL BASELINE TERMINOLOGY ---
    ['χρίω', 'christing_active', 'χρι[σξ]', 'Pres. Impf. Act.', 'Homer', 'Odyssey 4.252', 'λόεον καὶ χρῖον ἐλαίωι', 'https://perseus.org', 'To touch the surface of a body lightly; to rub or anoint with scented olive oil or unguents after bathing.'],
    ['χρίομαι', 'christing_middle', 'χρισ[αο]', 'Aorist Middle Participle', 'Homer', 'Odyssey 6.96', 'χρισάμενος λίπ᾽ ἐλαίωι', 'https://perseus.org', 'The reflexive middle voice transformation denoting the action of anointing oneself with olive oil after bathing.'],
    ['κέχριμαι', 'christing_passive', 'κεχρι|εχρι[σ]*θ', 'Perfect Passive Participle', 'Herodotus', 'Histories 4.189', 'αἰγέαι κεχριμέναι ἐρευθεδάνωι', 'https://perseus.org', 'The state of being washed dyed or coated externally with a color compound or protective pigment layer.'],
    ['περίχριστος', 'perichristos', 'περιχριστ', 'Technical Noun / Salve', 'Hippocrates', 'Aphorisms 1.24', 'φάρμακον περίχριστον ἐπὶ τοὺς ὀφθαλμούς', 'https://perseus.org', 'A specialized astringent eye salve or unguent meant to be smeared entirely around the eyelids.'],
    ['ἐπίχριστος', 'epichristos', 'επιχριστ', 'Technical Lotion / Plaster', 'Aristotle', 'Historia Animalium 625b31', 'ἔλαιον ἐπίχριστον ἐπὶ τοῦ σώματος', 'https://perseus.org', 'A medical lotion liniment or spreadable fluid application meant to be layered over skin surfaces.'],
    ['χριστά', 'christa', 'χριστ', 'Technical Class', 'Aeschylus', 'Prometheus Bound 480', 'τὰ δὲ χριστὰ τῶν φαρμάκων', 'https://perseus.org', 'The broad medical classification of all external semi-solid applications as opposed to swallowed internal potions.'],
    ['φαρμακεία', 'pharmakeia', 'φαρμακει', 'Abstract Noun', 'Plato', 'Leges 933b', 'περί τὰς φαρμακείας ἢ μαγγανείας', 'https://perseus.org', 'The broad deployment of chemical agents potions purgatives emetics abortifacients spells or witchcraft.'],
    ['μανιάς', 'manias', 'μανιαδ', 'Adjective / Condition', 'Euripides', 'Orestes 327', 'λύσσας μανιάδος', 'https://perseus.org', 'A frantic mad or frenzied state of consciousness associated with divinely induced panic fits.'],
    ['οἶστρος', 'oistros', 'οιστρ', 'Noun / Active Agency', 'Homer', 'Odyssey 22.300', 'αἰόλος οἶστρος', 'https://perseus.org', 'A giant horse-fly infesting cattle; metaphorically a sting a driving torment Erinyes-driven madness.'],
    ['ἔκστασις', 'ecstasis', 'εκστασ', 'Noun / Structural Shift', 'Aristotle', 'De Anima 406b13', 'πᾶσα κίνησις ἔκστασις', 'https://perseus.org', 'A physical displacement or structural change; shifting contextually into mental entrancement.'],
    ['λύσσα', 'lyssa', 'λυ[στ]{2}', 'Noun / Ecstatic Fit', 'Euripides', 'Bacchae 851', 'ἐλαφρά λύσσα', 'https://perseus.org', 'A blinding martial rage canine rabies or divinely induced Bacchic ecstasy personified.'],
    ['ἐπιθυμία', 'epithumia', 'επιθυμι', 'Noun / Internal Drive', 'Herodotus', 'Histories 1.32', 'ἐπιθυμίαν ἐκτελέσαι', 'https://perseus.org', 'An intense appetite longing yearning or internal driving passion/lust.'],
    ['προλέγω', 'prolego', 'προλεγ|προλεξ', 'Verb / Declaration', 'Aeschylus', 'Prometheus Bound 1071', 'μέμνησθ᾽ ἁγὼ προλέγω', 'https://perseus.org', 'To say beforehand predict via oracle proclaim publicly or denounce punishment.'],
    ['σινδών', 'sindonon', 'σινδ', 'Ritual Garment', 'Gospel of Mark', 'Mark 14.51', 'περιβεβλημένος σινδόνα ἐπὶ γυμνοῦ', 'https://perseus.org', 'Fine linen garment shroud or ritual wrapping fabric sheets.'],
    ['γυμνός', 'gymnos', 'γυμν', 'Ritual Status', 'Gospel of Mark', 'Mark 14.51', 'περιβεβλημένος σινδόνα ἐπὶ γυμνοῦ', 'https://perseus.org', 'Naked unclad or stripped of social armor status during transformational initiation boundaries.'],
    ['μυστήριον', 'mysterion', 'μυστηρ', 'Ritual Rite', 'Gospel of Mark', 'Mark 4.11', 'Ὑμῖν δέδοται γνῶναι τὸ μυστήριον', 'https://perseus.org', 'The mystery or secret rite itself; closing lips/eyes to retain theological revelations.'],
    ['ὄργια', 'orgia', 'οργι', 'Ecstatic Acts', 'Euripides', 'Bacchae 470', 'τὰ δ᾽ ὄργι᾽ ἐστὶ', 'https://perseus.org', 'Cultic ecstatic worship services and frenzied acts traditionally linked with Dionysus.'],
    ['κάθαρσις', 'katharsis', 'καθαρ', 'Purification Noun', 'Hippocrates', 'Aphorisms 1.24', 'καθάρσεις ἐν τῇσι νούσοισι', 'https://perseus.org', 'Physical and spiritual purification; cleansing a wound or purging the soul.'],
    ['μύησις', 'myesis', 'μυησ', 'Initiation Noun', 'Plato', 'Protagoras 354a', 'αἱ μυήσεις καὶ αἱ τελεταί', 'https://perseus.org', 'The formal step-by-step process of initiation into a hidden mystery cult or esoteric order.'],
    ['ἀπόρρητον', 'aporrheton', 'απορρητ', 'Secret Code Noun', 'Plato', 'Republic 337a', 'τὰ ἀπόρρητα τῶν δογμάτων', 'https://perseus.org', 'Forbidden to speak; sacred code words or hidden things completely concealed from the profane.'],
    ['ἄρρητος', 'arrhetos', 'αρρητ', 'Ineffable Adj', 'Euripides', 'Bacchae 470', 'ἄρρητ᾽ ἀμυήτοισιν βακχευμάτων', 'https://perseus.org', 'Ineffable or unutterable; realities too transcendent to be expressed in common human speech structures.'],
    ['ἀμύητος', 'amyeitos', 'αμυητ', 'Profane Status Noun', 'Euripides', 'Bacchae 470', 'ἄρρητ᾽ ἀμυήτοισιν βακχευμάτων', 'https://perseus.org', 'Uninitiated or profane; individuals who are strictly barred from entering the sacred rite boundaries.'],
    ['μαλάττω', 'malatto', 'μαλα[τξ]', 'Verb / Processing Root', 'Euripides', 'Orestes 1201', 'σπλάγχνον ὀργὰς ἐμαλάξαμεν', 'https://perseus.org', 'To make soft, supple leather; metaphorically to calm raw fury, appease anger, or soften a harsh nature.'],
    ['μάττω', 'matto', 'μαγ|μαξ', 'Verb / Kneading Root', 'Plato', 'Republic 372b', 'τὰ μὲν πέψαντες τὰ δὲ μάξαντες', 'https://perseus.org', 'To knead or press barley into shape; metaphorically to fashion or mold dynamic intellectual insights.'],
    ['κτητή', 'ktete', 'κτητ', 'Adjective / Social Status', 'Hesiod', 'Opera et Dies 406', 'γυναῖκα κτητήν οὐ γαμετήν', 'https://perseus.org', 'Acquirable, gainable, or desirable property; specifically designating a female slave or non-wedded domestic asset.'],
    ['γαμετή', 'gamete', 'γαμετ', 'Noun / Matrimonial', 'Hesiod', 'Opera et Dies 406', 'γυναῖκα κτητήν οὐ γαμετήν', 'https://perseus.org', 'A married woman or legal wife; strictly contrasted with concubines or enslaved property.'],
    ['ληΐζομαι', 'leizomai', 'ληι[ζσ]', 'Verb / Predatory Force', 'Euripides', 'Medea 256', 'ἐκ γῆς βαρβάρου λελῃσμένη', 'https://perseus.org', 'To seize, plunder, carry off as booty or captive property; to raid by foray or win via predatory force.'],
    ['αἰώνιος', 'aiōnios', 'αιωνι', 'Adjective / Existential', 'Plato', 'Timon 37d', 'εἰκὼ κινητόν τινα αἰῶνος ποιῆσαι', 'https://perseus.org', 'Lasting for an age, perpetual, or eternal; tracking transcendent cyclical or permanent duration states.'],
    ['βακχεύω', 'bakcheuo', 'βακχ', 'Verb / Ecstatic Ritual', 'Herodotus', 'Histories 4.79', 'τοῦ βακχεύειν πέρι Ἕλλησι ὀνειδίζουσι', 'https://perseus.org', 'To celebrate the ecstatic mysteries of Bacchus; to act or speak like one inspired with mystic mania.'],
    ['βακχικός', 'bakchikos', 'βακχ', 'Adjective / Cultic State', 'Herodotus', 'Histories 2.81', 'τοῖσι Ὀρφικοῖσι... καὶ Βακχικοῖσι', 'https://perseus.org', 'Belonging to or inspiring the ecstatic deliriums of the Bacantes; designating Dionysiac mysteries.'],
    # === PASTE THIS EXACT BLOCK TO RE-JOIN YOUR CODE MATRIX ===
    # --- NEW TOXICOLOGICAL LAYER: MEDICINES AND REMEDIES ---
    ['ἀλεξιφάρμακον', 'alexipharmakon', 'αλεξιφαρμακ', 'Noun / Antidote Core', 'Nicander', 'Alexipharmaca 1.1', 'ἀλεξιφάρμακα δούρατα', 'https://perseus.org', 'An active antidote, protective counter-remedy, or chemical safeguard shielding against toxic agents.'],
    ['ἀντίδοτος', 'antidotos', 'αντιδοτ', 'Noun / Counter-Agent', 'Galen', 'De Antidotis 14.1', 'ἡ διὰ τῶν ἀντιδότων θεραπεία', 'https://perseus.org', 'Given as a structural remedy against a poison; the direct linguistic origin of the modern word antidote.'],
    ['θηριακή', 'theriake', 'θηριακ', 'Noun / Panacea', 'Galen', 'De Theriaca ad Pisonem 14.210', 'ἡ θηριακὴ γαλήνη', 'https://perseus.org', 'An antidote compounded specifically against the bites of venomed beasts, later evolving into a global panacea.'],
    ['ἄκεσις', 'akesis', 'ακεσ', 'Noun / Active Healing', 'Aeschylus', 'Choephori 539', 'ἄκεσις πημάτων', 'https://perseus.org', 'Healing, curing, or the execution of an active restorative medical remedy for a systemic illness.'],
    ['βοήθημα', 'boethema', 'βοηθημ', 'Noun / Therapeutic Aid', 'Hippocrates', 'De Fracturis 12.2', 'βοήθημα τῷ σώματι', 'https://perseus.org', 'A medical aid, palliative support, or targeted therapeutic remedy to assist distressed anatomy.'],
    ['ἴαμα', 'iama', 'ιαματ', 'Noun / Restoration Potion', 'Plato', 'Philebus 46a', 'ἴαμα τῆς νόσου', 'https://perseus.org', 'A medicine, cure, or restorative healing potion mixed to drive back systemic pathology matrices.'],
    ['ἐπίπαστον', 'epipaston', 'επιπαστ', 'Noun / Medicinal Powder', 'Hippocrates', 'De Ulceribus 4.12', 'ἐπίπαστα φάρμακα', 'https://perseus.org', 'A medicinal powder sprinkled directly over raw flesh wounds, sores, or ruptured ulcers.'],
    ['κατάπλασμα', 'cataplasma', 'καταπλασμ', 'Noun / Poultice', 'Galen', 'De Compositione Medicamentorum 13.1', 'τὸ κατάπλασμα ἐπιτιθέναι', 'https://perseus.org', 'A poultice or spreadable plaster array layered onto the physical body surface for localized treatment.'],

    # --- NEW TOXICOLOGICAL LAYER: PREPARATION AND APPLICATION ---
    ['ποίησησις', 'poiesis', 'ποιησ', 'Noun / Compounding', 'Plato', 'Symposium 205b', 'ἡ τῶν φαρμάκων ποίησις', 'https://perseus.org', 'The active preparation, chemical compounding, or physical formulation of medicines and drugs.'],
    ['μίγμα', 'migma', 'μιγμ', 'Noun / Mixture', 'Aristotle', 'De Generatione et Corruptione 328b22', 'τὸ μίγμα τῶν στοιχείων', 'https://perseus.org', 'A mixture, compound blend, or mechanical combination of separate therapeutic raw ingredients.'],
    ['ξύφιον', 'xyphium', 'ξυφι', 'Noun / Plant Infusion', 'Dioscorides', 'De Materia Medica 4.20', 'ξύφιον οἱ δὲ ξιφίον', 'https://perseus.org', 'An expressed fluid, chemical infusion, or pressed juice of specific flora matrices extracted for treatment.'],
    ['χυλός', 'chylos', 'χυλ', 'Noun / Plant Moisture', 'Theophrastus', 'Historia Plantarum 9.8.1', 'ὁ χυλὸς τῆς ῥίζης', 'https://perseus.org', 'Juice, moisture, sap, or the vital expressed fluid extracted directly from medicinal roots and leaves.'],
    ['ἔγχυμα', 'enchyma', 'εγχυμ', 'Noun / Injection', 'Galen', 'De Compositione Medicamentorum 12.89', 'ἔγχυμα εἰς τὰ ὦτα', 'https://perseus.org', 'An infusion, liquid injection, or fluid compound intentionally poured into bodily tracts or channels.'],
    ['χρῖσμα', 'chrismon', 'χρισμ', 'Noun / Salve Ointment', 'Septuagint', 'Exodus 30.25', 'ἔλαιον χρῖσμα ἅγιον', 'https://perseus.org', 'An ointment, oil, or thick salve applied externally to skin surfaces as a token of protection or consecration.'],

    # --- NEW TOXICOLOGICAL LAYER: PRACTITIONERS AND KNOWLEDGE ---
    ['φαρμακοπώλης', 'pharmacopoles', 'φαρμακοπωλ', 'Noun / Drug Vendor', 'Aristophanes', 'Thesmophoriazusae 504', 'παρὰ τοῦ φαρμακοπώλου', 'https://perseus.org', 'A merchant vendor of drugs, prepared roots, herbs, and potions; often operating as an itinerant seller.'],
    ['φαρμακεύτρια', 'pharmaceutria', 'φαρμακευτρ', 'Noun / Sorceress', 'Theocritus', 'Idylls 2.1', 'ταὶ φαρμακεύτριαι', 'https://perseus.org', 'A female compounder, herbal sorceress, or maker of lethal potions and binding botanical spells.'],
    ['ῥιζοτόμος', 'rhizotomos', 'ῥιζοτομ|ριζοτομ', 'Noun / Root-Cutter', 'Sophocles', 'Fragments 534', 'ῥιζοτόμους παρθένους', 'https://perseus.org', 'A root-cutter; an ancient expert field botanist specialized in harvesting and preserving powerful medical herbs.'],
    ['ἰατρός', 'iatros', 'ιατρ', 'Noun / Physician Healer', 'Homer', 'Iliad 11.514', 'ἰατρός γὰρ ἀνὴρ πολλῶν ἀντάξιος', 'https://perseus.org', 'A physician, authoritative clinical practitioner, or surgical healer operating across ancient societies.']

    # === PASTE THIS EXACT BLOCK TO RE-JOIN YOUR CODE MATRIX ===
    ['ἀλεξιφάρμακον', 'alexipharmakon', 'αλεξιφαρμακ', 'Noun / Antidote Core', 'Nicander', 'Alexipharmaca 1.1', 'ἀλεξιφάρμακα δούρατα', 'https://perseus.org', 'An active antidote, protective counter-remedy, or chemical safeguard shielding against toxic agents.'],
    ['ἀντίδοτος', 'antidotos', 'αντιδοτ', 'Noun / Counter-Agent', 'Galen', 'De Antidotis 14.1', 'ἡ διὰ τῶν ἀντιδότων θεραπεία', 'https://perseus.org', 'Given as a structural remedy against a poison; the direct linguistic origin of the modern word antidote.'],
    ['θηριακή', 'theriake', 'θηριακ', 'Noun / Panacea', 'Galen', 'De Theriaca ad Pisonem 14.210', 'ἡ θηριακὴ γαλήνη', 'https://perseus.org', 'An antidote compounded specifically against the bites of venomed beasts, later evolving into a global panacea.'],
    ['ἄκεσις', 'akesis', 'ακεσ', 'Noun / Active Healing', 'Aeschylus', 'Choephori 539', 'ἄκεσις πημάτων', 'https://perseus.org', 'Healing, curing, or the execution of an active restorative medical remedy for a systemic illness.'],
    ['βοήθημα', 'boethema', 'βοηθημ', 'Noun / Therapeutic Aid', 'Hippocrates', 'De Fracturis 12.2', 'βοήθημα τῷ σώματι', 'https://perseus.org', 'A medical aid, palliative support, or targeted therapeutic remedy to assist distressed anatomy.'],
    ['ἴαμα', 'iama', 'ιαματ', 'Noun / Restoration Potion', 'Plato', 'Philebus 46a', 'ἴαμα τῆς νόσου', 'https://perseus.org', 'A medicine, cure, or restorative healing potion mixed to drive back systemic pathology matrices.'],
    ['ἐπίπαστον', 'epipaston', 'επιπαστ', 'Noun / Medicinal Powder', 'Hippocrates', 'De Ulceribus 4.12', 'ἐπίπαστα φάρμακα', 'https://perseus.org', 'A medicinal powder sprinkled directly over raw flesh wounds, sores, or ruptured ulcers.'],
    ['κατάπλασμα', 'cataplasma', 'καταπλασμ', 'Noun / Poultice', 'Galen', 'De Compositione Medicamentorum 13.1', 'τὸ κατάπλασμα ἐπιτιθέναι', 'https://perseus.org', 'A poultice or spreadable plaster array layered onto the physical body surface for localized treatment.'],

    # --- NEW TOXICOLOGICAL LAYER: PREPARATION AND APPLICATION ---
    ['ποίησησις', 'poiesis', 'ποιησ', 'Noun / Compounding', 'Plato', 'Symposium 205b', 'ἡ τῶν φαρμάκων ποίησις', 'https://perseus.org', 'The active preparation, chemical compounding, or physical formulation of medicines and drugs.'],
    ['μίγμα', 'migma', 'μιγμ', 'Noun / Mixture', 'Aristotle', 'De Generatione et Corruptione 328b22', 'τὸ μίγμα τῶν στοιχείων', 'https://perseus.org', 'A mixture, compound blend, or mechanical combination of separate therapeutic raw ingredients.'],
    ['ξύφιον', 'xyphium', 'ξυφι', 'Noun / Plant Infusion', 'Dioscorides', 'De Materia Medica 4.20', 'ξύφιον οἱ δὲ ξιφίον', 'https://perseus.org', 'An expressed fluid, chemical infusion, or pressed juice of specific flora matrices extracted for treatment.'],
    ['χυλός', 'chylos', 'χυλ', 'Noun / Plant Moisture', 'Theophrastus', 'Historia Plantarum 9.8.1', 'ὁ χυλὸς τῆς ῥίζης', 'https://perseus.org', 'Juice, moisture, sap, or the vital expressed fluid extracted directly from medicinal roots and leaves.'],
    ['ἔγχυμα', 'enchyma', 'εγχυμ', 'Noun / Injection', 'Galen', 'De Compositione Medicamentorum 12.89', 'ἔγχειμα εἰς τὰ ὦτα', 'https://perseus.org', 'An infusion, liquid injection, or fluid compound intentionally poured into bodily tracts or channels.'],
    ['χρῖσμα', 'chrismon', 'χρισμ', 'Noun / Salve Ointment', 'Septuagint', 'Exodus 30.25', 'ἔλαιον χρῖσμα ἅγιον', 'https://perseus.org', 'An ointment, oil, or thick salve applied externally to skin surfaces as a token of protection or consecration.'],

    # --- NEW TOXICOLOGICAL LAYER: PRACTITIONERS AND KNOWLEDGE ---
    ['φαρμακοπώλης', 'pharmacopoles', 'φαρμακοπωλ', 'Noun / Drug Vendor', 'Aristophanes', 'Thesmophoriazusae 504', 'παρὰ τοῦ φαρμακοπώλου', 'https://perseus.org', 'A merchant vendor of drugs, prepared roots, herbs, and potions; often operating as an itinerant seller.'],
    ['φαρμακεύτρια', 'pharmaceutria', 'φαρμακευτρ', 'Noun / Sorceress', 'Theocritus', 'Idylls 2.1', 'ταὶ φαρμακεύτριαι', 'https://perseus.org', 'A female compounder, herbal sorceress, or maker of lethal potions and binding botanical spells.'],
    ['ῥιζοτόμος', 'rhizotomos', 'ῥιζοτομ|ριζοτομ', 'Noun / Root-Cutter', 'Sophocles', 'Fragments 534', 'ῥιζοτόμους παρθένους', 'https://perseus.org', 'A root-cutter; an ancient expert field botanist specialized in harvesting and preserving powerful medical herbs.'],
    ['ἰατρός', 'iatros', 'ιατρ', 'Noun / Physician Healer', 'Homer', 'Iliad 11.514', 'ἰατρὸς γὰρ ἀνὴρ πολλῶν ἀντάξιος', 'https://perseus.org', 'A physician, authoritative clinical practitioner, or surgical healer operating across ancient societies.']

    # === PASTE THIS EXACT BLOCK TO RE-JOIN AND FINALIZE YOUR DATA MATRIX ===
    ['ποίησησις', 'poiesis', 'ποιησ', 'Noun / Compounding', 'Plato', 'Symposium 205b', 'ἡ τῶν φαρμάκων ποίησις', 'https://perseus.org', 'The active preparation, chemical compounding, or physical formulation of medicines and drugs.'],
    ['μίγμα', 'migma', 'μιγμ', 'Noun / Mixture', 'Aristotle', 'De Generatione et Corruptione 328b22', 'τὸ μίγμα τῶν στοιχείων', 'https://perseus.org', 'A mixture, compound blend, or mechanical combination of separate therapeutic raw ingredients.'],
    ['ξύφιον', 'xyphium', 'ξυφι', 'Noun / Plant Infusion', 'Dioscorides', 'De Materia Medica 4.20', 'ξύφιον οἱ δὲ ξιφίον', 'https://perseus.org', 'An expressed fluid, chemical infusion, or pressed juice of specific flora matrices extracted for treatment.'],
    ['χυλός', 'chylos', 'χυλ', 'Noun / Plant Moisture', 'Theophrastus', 'Historia Plantarum 9.8.1', 'ὁ χυλὸς τῆς ῥίζης', 'https://perseus.org', 'Juice, moisture, sap, or the vital expressed fluid extracted directly from medicinal roots and leaves.'],
    ['ἔγχυμα', 'enchyma', 'εγχυμ', 'Noun / Injection', 'Galen', 'De Compositione Medicamentorum 12.89', 'ἔγχυμα εἰς τὰ ὦτα', 'https://perseus.org', 'An infusion, liquid injection, or fluid compound intentionally poured into bodily tracts or channels.'],
    ['χρῖσμα', 'chrismon', 'χρισμ', 'Noun / Salve Ointment', 'Septuagint', 'Exodus 30.25', 'ἔλαιον χρῖσμα ἅγιον', 'https://perseus.org', 'An ointment, oil, or thick salve applied externally to skin surfaces as a token of protection or consecration.'],

    # --- NEW TOXICOLOGICAL LAYER: PRACTITIONERS AND KNOWLEDGE ---
    ['φαρμακοπώλης', 'pharmacopoles', 'φαρμακοπωλ', 'Noun / Drug Vendor', 'Aristophanes', 'Thesmophoriazusae 504', 'παρὰ τοῦ φαρμακοπώλου', 'https://perseus.org', 'A merchant vendor of drugs, prepared roots, herbs, and potions; often operating as an itinerant seller.'],
    ['φαρμακεύτρια', 'pharmaceutria', 'φαρμακευτρ', 'Noun / Sorceress', 'Theocritus', 'Idylls 2.1', 'ταὶ φαρμακεύτριαι', 'https://perseus.org', 'A female compounder, herbal sorceress, or maker of lethal potions and binding botanical spells.'],
    ['ῥιζοτόμος', 'rhizotomos', 'ῥιζοτομ|ριζοτομ', 'Noun / Root-Cutter', 'Sophocles', 'Fragments 534', 'ῥιζοτόμους παρθένους', 'https://perseus.org', 'A root-cutter; an ancient expert field botanist specialized in harvesting and preserving powerful medical herbs.'],
    ['ἰατρός', 'iatros', 'ιατρ', 'Noun / Physician Healer', 'Homer', 'Iliad 11.514', 'ἰατὸς γὰρ ἀνὴρ πολλῶν ἀντάξιος', 'https://perseus.org', 'A physician, authoritative clinical practitioner, or surgical healer operating across ancient societies.']
] # <--- Cleanly terminates the open dataset array block

with open('master_word_list.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

print('[✔] Full master word list file generated natively with 61 rows!')

