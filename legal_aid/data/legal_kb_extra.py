# Additional Pakistani Legal Knowledge Base Entries
# Drop this file into: legal_aid/data/legal_kb_extra.py
#
# These are NEW entries that extend the existing LEGAL_KNOWLEDGE list in legal_kb.py
# without touching/duplicating what's already there.
#
# HOW TO USE — Add these 2 lines to the end of legal_kb.py:
#
#     from data.legal_kb_extra import EXTRA_LEGAL_KNOWLEDGE
#     LEGAL_KNOWLEDGE.extend(EXTRA_LEGAL_KNOWLEDGE)
#
# (Full instructions also given separately below.)

EXTRA_LEGAL_KNOWLEDGE = [
    {
        "id": "inheritance_001",
        "category": "Family Law",
        "title": "Inheritance / Wirasat / Property Distribution",
        "content": """
Inheritance in Pakistan is governed by Islamic Law (Sharia) for Muslims under the 
Muslim Personal Law (Shariat) Application Act 1962, and the West Pakistan Muslim 
Personal Law (Shariat) Application Act for specific provincial matters.

BASIC SHARES (simplified — actual shares depend on family composition):
- Son: Gets double the share of a daughter
- Daughter: Entitled to a fixed share, cannot be excluded
- Widow: 1/8 share if there are children, 1/4 if no children
- Parents: Entitled to fixed shares depending on other heirs present

SUCCESSION CERTIFICATE:
- Required to claim bank accounts, shares, and movable property of deceased
- Apply to Civil Court (or NADRA in some areas under simplified process)
- Required documents: Death certificate, family tree (Shajra), CNIC copies

MUTATION OF INHERITED PROPERTY (Intiqal):
- Apply at local Patwari/Land Revenue office for agricultural land
- Apply at relevant housing authority for urban property
- All legal heirs must consent or be given notice

DISPUTES:
- If a legal heir is denied their share, file a civil suit for partition in Civil Court
- Can also approach Arbitration Council for family settlement first

Relevant law: Muslim Personal Law (Shariat) Application Act 1962, Succession Act 1925 (for procedural matters)
        """,
        "keywords": ["inheritance", "wirasat", "succession", "property distribution", "legal heir", "wills", "vaarsi", "وراثت", "جائیداد کی تقسیم", "وارث"]
    },
    {
        "id": "domestic_violence_001",
        "category": "Family Law",
        "title": "Domestic Violence / Dowry Harassment",
        "content": """
Domestic violence in Pakistan is addressed under provincial laws:
- Punjab Protection of Women Against Violence Act 2016
- Sindh Domestic Violence (Prevention and Protection) Act 2013
- KPK Domestic Violence Against Women (Prevention and Protection) Act 2021
- Balochistan Domestic Violence (Prevention and Protection) Act (where enacted)

PROTECTION AVAILABLE:
- Protection Order: Restrains abuser from contacting/approaching victim
- Residence Order: Allows victim to stay in shared household
- Monetary relief for medical expenses, lost earnings

DOWRY-RELATED HARASSMENT:
- Dowry and Bridal Gifts (Restriction) Act 1976 limits excessive dowry demands
- Harassment for dowry can be reported alongside domestic violence complaints
- Can also file under Section 506 PPC (criminal intimidation) if threats are made

HOW TO FILE:
1. Approach Women Protection Officer / District Women Protection Committee
2. File application at Family Court or Magistrate Court for protection order
3. Can simultaneously file police complaint under PPC if physical assault occurred
4. Helpline: 1043 (Punjab Women Helpline), or local Edhi/Madadgar helplines

EVIDENCE TO COLLECT:
- Medical reports of injuries
- Photos/videos (where safe to obtain)
- Witness statements from neighbors/family
- Any written threats (messages, letters)

Relevant courts: Family Court, Magistrate Court (1st Class)
        """,
        "keywords": ["domestic violence", "dowry", "harassment", "abuse", "beating", "wife beating", "jahez", "گھریلو تشدد", "جہیز", "زیادتی"]
    },
    {
        "id": "traffic_001",
        "category": "Criminal Law",
        "title": "Traffic Violations / Road Accidents",
        "content": """
Traffic matters in Pakistan fall under the Motor Vehicles Ordinance 1965 and 
provincial Traffic Police rules, with serious accidents also invoking the Pakistan Penal Code.

ROAD ACCIDENT WITH INJURY/DEATH:
- File FIR immediately at nearest police station under Section 279 PPC (rash driving) 
  and Section 320/337/338 PPC depending on severity of injury
- If death occurs: Section 302/304-A PPC may apply (culpable homicide not amounting to murder)
- Compensation can be claimed under Motor Vehicles Ordinance via Motor Accident Claims Tribunal

CHALLAN / TRAFFIC FINES:
- Can be contested at Traffic Court if believed to be wrongly issued
- Must be paid within stipulated time or fine increases

HIT AND RUN:
- Report immediately to Traffic Police and nearest Police Station
- Note vehicle registration number, time, location if possible
- CCTV footage from nearby shops/cameras can be requested as evidence

INSURANCE CLAIMS (if vehicle insured):
- Notify insurance company within 24-48 hours of accident
- File claim with police report (FIR/Daily Diary entry) attached

COMPENSATION FOR VICTIMS:
- Can file civil suit for damages in addition to criminal case
- Motor Accident Claims Tribunal handles compensation claims specifically for road accidents

Relevant law: Motor Vehicles Ordinance 1965, PPC Sections 279, 304-A, 337, 338
        """,
        "keywords": ["accident", "traffic", "challan", "hit and run", "road accident", "driving", "vehicle", "ٹریفک", "حادثہ", "گاڑی"]
    },
    {
        "id": "general_001",
        "category": "Unknown",
        "title": "General Legal Guidance / Unclassified Matters",
        "content": """
This entry is used when a citizen's problem does not clearly fit into one of the 
seven main legal categories (Labor, Consumer, Property, Family, Cyber, Criminal, Banking).

GENERAL FIRST STEPS FOR ANY LEGAL ISSUE:
1. Write down a clear timeline of events with dates
2. Collect all relevant documents (contracts, receipts, messages, photos)
3. Identify witnesses who can support your account
4. Consult a local lawyer/advocate for matters not covered by the categories above —
   especially for specialized areas like tax law, immigration, intellectual property, 
   constitutional petitions, or corporate/business disputes

WHERE TO GET FREE/LOW-COST LEGAL HELP IN PAKISTAN:
- District Legal Aid Committees (under Access to Justice Programme)
- Pakistan Bar Council Legal Aid Cell
- Local Bar Association free legal aid clinics (most district bar associations offer this)
- Human Rights Cell, Ministry of Human Rights (for human rights violations): 1099

WHEN TO ESCALATE TO A SPECIALIZED LAWYER:
- Constitutional matters (writ petitions) → High Court advocate required
- Tax disputes → Tax lawyer / consult FBR's helpline 051-111-772-772
- Immigration/passport issues → Contact relevant Ministry of Interior office
- Business/corporate disputes → Corporate lawyer, may involve SECP

Relevant body: Pakistan Bar Council, District Bar Associations
        """,
        "keywords": ["general", "unsure", "other", "unclassified", "help", "legal advice", "مدد", "وکیل"]
    }
]
