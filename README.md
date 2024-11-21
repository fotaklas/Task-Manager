# Task-Manager
Ένα απλό εργαλείο για τη διαχείριση των καθημερινών σου tasks, σχεδιασμένο για ευκολία και φορητότητα με Docker!

Χαρακτηριστικά
Προσθήκη νέων tasks με στόχους σε ώρες.
Ενημέρωση χρόνου που αφιερώνεις σε κάθε task.
Αναφορά στο τέλος της ημέρας για το τι ολοκληρώθηκε και τι όχι.
Φορητό μέσω Docker για να τρέχει παντού χωρίς εξαρτήσεις.
Προαπαιτούμενα
Docker,
Python 3.10+ (προαιρετικό, αν δεν χρησιμοποιήσεις Docker).
Οδηγίες Εγκατάστασης
1. Κλώνος του Αποθετηρίου
bash
Copy code
git clone https://github.com/fotaklas/Task-Manager.git
cd task-manager
2. Δημιουργία του Docker Image
bash
Copy code
docker build -t task-manager .
Πώς να το Χρησιμοποιήσεις
Με Docker
Εκκίνηση του Task Manager:

bash
Copy code
docker run -it --rm task-manager
Ακολούθησε τις οδηγίες στο τερματικό για να προσθέσεις, ενημερώσεις ή να δεις τα tasks σου.

Παραδείγματα Χρήσης
Προσθήκη Task
Όνομα: LeetCode
Στόχος: 2 ώρες
text
Copy code
1. Προσθήκη Task
Όνομα Task: LeetCode
Στόχος (σε ώρες): 2
Το task 'LeetCode' προστέθηκε με στόχο 2 ώρες.
Ενημέρωση Task
Task: LeetCode
Χρόνος εργασίας: 1 ώρα
text
Copy code
2. Ενημέρωση Task
Όνομα Task: LeetCode
Χρόνος που δούλεψες (σε ώρες): 1
Προστέθηκαν 1 ώρες στο task 'LeetCode'.
Αναφορά Ημέρας
text
Copy code
--- Αναφορά Ημέρας ---
LeetCode: 1 ώρες από 2 στόχο.
❌ Δεν ολοκληρώθηκε.
------------------------

Συμμετοχή
Είσαι ευπρόσδεκτος να κάνεις fork το project, να προσθέσεις λειτουργίες, και να στείλεις ένα pull request.
Αν έχεις ιδέες ή βρήκες bugs, άνοιξε ένα issue.


