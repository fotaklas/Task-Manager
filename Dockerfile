# Χρησιμοποιούμε την Python ως βάση
FROM python:3.10-slim

# Ορίζουμε τον κατάλογο εργασίας μέσα στο container
WORKDIR /app

# Αντιγράφουμε το αρχείο task_manager.py στο container
COPY main.py .

# Αν υπάρχουν εξωτερικές βιβλιοθήκες, μπορούμε να τις προσθέσουμε (π.χ., requirements.txt)
# Αν όχι, αγνοούμε αυτό το βήμα
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Εκκίνηση του προγράμματος
CMD ["python", "main.py"]
