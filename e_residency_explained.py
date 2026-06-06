"""Explains how Estonia's e-Residency program works, step by step."""

STEPS = [
    ("1. What it is",
     "e-Residency is a government-issued digital identity. It is NOT citizenship, "
     "physical residency, or a visa — it does not grant the right to live in or "
     "enter Estonia."),

    ("2. Who can apply",
     "Any person from any country in the world (18+) can apply online by filling "
     "out a form, stating their motivation, and paying a state fee."),

    ("3. Background check",
     "Estonian Police and Border Guard run a background check on every applicant "
     "to prevent misuse (fraud, money laundering, etc.)."),

    ("4. Pickup of the digital ID card",
     "Once approved, the applicant picks up a smart ID card (with chip and PIN "
     "codes) at an Estonian embassy/consulate or a designated pickup point."),

    ("5. Digital identity & signing",
     "The card lets the e-resident authenticate online and give legally binding "
     "digital signatures (valid across the EU under eIDAS), using a card reader "
     "or the Smart-ID/Mobile-ID apps."),

    ("6. Starting and running a company",
     "e-Residents can remotely register an Estonian company (usually an OÜ, a "
     "private limited company) via the e-Business Register, entirely online."),

    ("7. Running the business online",
     "They can sign documents and contracts digitally, open accounts with "
     "fintechs/banks that accept e-Residents, manage accounting through "
     "e-services, and submit tax declarations to the Estonian Tax Board online."),

    ("8. Taxes",
     "The company pays Estonian corporate tax rules (notably 0% tax on retained, "
     "reinvested profits — tax is due only on distributed profits). The "
     "e-resident's personal tax residency is determined separately, by where "
     "they actually live, not by e-Residency."),

    ("9. EU market access",
     "Because Estonia is in the EU, an Estonian company gives access to the EU "
     "single market and EU business infrastructure (payments, invoicing, etc.)."),

    ("10. Renewal & limits",
     "The digital ID card is valid for a set number of years and can be renewed. "
     "e-Residency can be revoked if misused. It is a tool for location-independent "
     "business administration, not a path to migration."),
]


def explain():
    print("How e-Residency in Estonia works\n" + "=" * 34)
    for title, description in STEPS:
        print(f"\n{title}\n{'-' * len(title)}\n{description}")


if __name__ == "__main__":
    explain()
