# Sample Files

This directory contains sample files used to reproduce the experiments in the paper.

## File Structure

```
├── code_augmentation/
│   └── sample.py
├── file_exfiltration/
│   └── non_sensitive.pdf
├── image_steganography/
│   ├── sample_small.png
│   └── sample_large.png
└── SAMPLES.md
```

## Note on Sensitive PDF

The sensitive PDF sample is **not included** in this repository to avoid publishing personally identifiable information, even in synthetic form.

To reproduce the sensitive file exfiltration scenario, create a PDF containing the following synthetic credentials:

- Email address
- Password string
- Credit card number
- Physical address

Any placeholder values are acceptable as long as they resemble the format of real credentials.
