# Dark Pattern Demonstration & Test Sites

This folder is **completely separate** from the main `clearclick-ai` codebase. It contains multi-page mock websites built specifically to demonstrate real-world deceptive design patterns (dark patterns) flagged by ClearClick AI.

---

## 📁 Directory Structure

```
dark-pattern-test-sites/
├── index.html                   # Central portal linking to all 3 demo sites
├── server.py                    # Optional 1-click local HTTP server (port 5000)
├── hotel-booking/               # Site 1: Azure Grand Hotel & Spa
│   ├── index.html               # Cookie consent asymmetry & missing reject button
│   ├── rooms.html               # Pre-ticked consent & double-negative opt-out
│   └── checkout.html            # Microprint mandatory resort fee ($45) & add-on insurance
├── subscription-service/        # Site 2: FitPulse Gym & Wellness Club
│   ├── index.html               # Low-contrast recurring membership disclaimer
│   ├── pricing.html             # Pre-ticked partner data sharing
│   └── account.html             # Confirm-shaming modal & buried cancellation link
└── ticket-hub/                  # Site 3: ConcertPass Live Tickets
    ├── index.html               # Event listings
    ├── event.html               # High-pressure urgency countdown timer (AIDUI)
    └── payment.html             # Drip pricing: $65 ticket inflates to $100 with fees
```

---

## 🎯 Flagged Patterns by Page

| Website | File | Dark Pattern Detected | What ClearClick AI Flags |
| :--- | :--- | :--- | :--- |
| **Azure Grand Hotel** | `hotel-booking/index.html` | `missing_reject_option`, `unequal_button_emphasis` | First-layer cookie banner has green "Accept All" with no direct "Reject" button. |
| **Azure Grand Hotel** | `hotel-booking/rooms.html` | `preticked_consent`, `double_negative_language` | Pre-ticked marketing checkbox + "Uncheck if you do not wish to not receive..." |
| **Azure Grand Hotel** | `hotel-booking/checkout.html` | `microprint_fee`, `low_contrast_fee` | Mandatory $45 resort fee hidden in 8px faint grey text. |
| **FitPulse Club** | `subscription-service/index.html` | `low_contrast_fee` | Auto-renewal term in low-contrast grey text failing WCAG. |
| **FitPulse Club** | `subscription-service/pricing.html` | `preticked_consent` | Pre-ticked partner telemetry and health data advertising sharing. |
| **FitPulse Club** | `subscription-service/account.html` | `confirm_shaming`, `buried_cancel_link` | "No thanks, I hate saving money..." button + cancel link buried in 10px footer. |
| **ConcertPass** | `ticket-hub/event.html` | `countdown_timer`, `high_demand_scarcity` | Fake countdown clock and artificial urgency message. |
| **ConcertPass** | `ticket-hub/payment.html` | `drip_pricing`, `preticked_consent` | Ticket jumps from $65 to $100 at final step via electronic/facility fees + pre-ticked insurance. |

---

## 🚀 How to Test in ClearClick AI

### Method 1: Upload HTML (Instant & Recommended)
1. Open your ClearClick AI scanner.
2. Click **"Upload Screenshot or HTML"**.
3. Drag and drop any `.html` file from this folder (e.g. `checkout.html`, `account.html`, or `payment.html`).
4. ClearClick AI will immediately render the visual proof markers, yellow bounding boxes, and evidence quotes.

### Method 2: Screenshot Upload
1. Double-click any of the `.html` files in this folder to open it in Chrome or your default browser.
2. Take a screenshot (`Win + Shift + S`).
3. Upload the screenshot to ClearClick AI to verify visual marker coordinate alignment.

### Method 3: Local HTTP Server
Run the included python server:
```bash
python server.py
```
Open `http://localhost:5000` in your browser to browse all 3 sites interactively.
