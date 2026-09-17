# Just CSE Archive

Personal long-term archive of university CSE coursework, study materials, laboratory work, and independent academic projects.

The archive preserves the original project files and nested Git repositories. Only outer folder names, locations, and archive documentation were changed to make the collection easier to navigate.

## Contents

```text
Year-1/          Year-1 coursework
Year-2/          Year-2 coursework
Year-3/          Year-3 coursework
Year-4/          Year-4 coursework
Projects/        Independent academic projects
Resources/       Books and general study materials
Uncategorized/   Items awaiting reliable classification
```

Each year contains `Semester-1/` and `Semester-2/`. Empty semester folders are intentional placeholders for future coursework.

## Course index

| Location | Course or subject | Contents |
| --- | --- | --- |
| `Year-1/Semester-2/Numerical-Methods/` | Numerical Methods | C++ implementations of numerical algorithms |
| `Year-2/Semester-1/CSE-2104-Algorithm/` | CSE-2104 Algorithm | Algorithm implementations and a separate assignment repository |
| `Year-3/Semester-1/CSE-3102-Operating-Systems/` | CSE-3102 Operating Systems | Operating-systems laboratory work |
| `Year-3/Semester-2/Assembly-Language-Programming/` | Assembly Language Programming | Assembly-language exercises |
| `Year-4/Semester-1/CSE-4016-Design-Patterns-Lab/` | CSE-4016 Design Patterns Lab | Design-pattern examples and technical demonstrations |
| `Year-4/Semester-1/CSE-4102-Computer-Graphics-and-Multimedia-Lab/` | CSE-4102 Computer Graphics and Multimedia | Python graphics laboratory work |

Course-level READMEs document the known course code, subject, contents, and technology. Where a formal code is not present in the source repository, it is marked as unknown rather than guessed.

## Project index

| Project | Description | Main technologies |
| --- | --- | --- |
| `Projects/Car-Showroom-Management-System/` | Car-showroom management and database project | Database/web technologies |
| `Projects/Decision-Tree-CART-vs-ID3/` | CART and ID3 comparison using the Adult Income dataset | Python, Jupyter Notebook |
| `Projects/Face-Recognition-Attendance-System/` | Face-recognition attendance application | Python, OpenCV, Dlib, MySQL |
| `Projects/Hotel-Management-System/` | Command-line hotel reservation system | Java |
| `Projects/Inventory-Management-Bakery/` | Bakery inventory and sales simulation | Python, pandas, NumPy, Matplotlib |
| `Projects/IoT-Weather-Monitoring-System/` | ESP32 weather monitoring system with web and database components | C/C++, PHP, JavaScript, SQL |
| `Projects/Just-Hall-Website/` | Hall-management web application | .NET and web technologies |
| `Projects/KNN-Loan-Prediction/` | KNN classification for loan approval prediction | Python, Jupyter Notebook |
| `Projects/Single-Server-Queue-Simulation-Python/` | Single-server queue simulation and Datathon notebook | Python, Jupyter Notebook |
| `Projects/SQL-Demo-Hall-Web/` | Demo-hall management database script | SQL |

Project-specific READMEs provide additional details when available. Notebook projects without dependency manifests are documented as preserved source archives rather than guaranteed reproducible environments.

## Resources

`Resources/Books/` contains the original book and study-material collection. Its existing semester folders are preserved:

- `semester-1-2/`
- `semester-2-1/`
- `semester-2-2/`
- `semester-3-1/`
- `semester-3-2/`
- `semester-4-1/`

Four oversized book PDFs remain preserved locally but are excluded from the GitHub commit because GitHub rejects files larger than 100 MB. Their exact paths are listed in the root `.gitignore`. The rest of the Books collection is included in the archive repository.

## Preservation and duplicate policy

- Source code, datasets, notebooks, documentation, images, and nested Git metadata are retained.
- Exact duplicate build and IDE-support files may occur inside separate technical demonstrations because each demonstration is a separate project.
- The duplicated AIS-3201 subtree found inside the CSE-3203 Books folder was removed after byte-for-byte comparison; the canonical AIS-3201 copy was retained.
- Source or project files were not removed when their location was meaningful to a separate project, even if their content matched another project file.
- Generated cache directories such as `__pycache__/`, `bin/`, `obj/`, and `.vs/` are not considered academic source duplicates.

## Privacy note

The face-recognition project contains images that may show identifiable people, attendance data, and trained model artifacts. Review consent, access permissions, and distribution requirements before publishing this archive.
