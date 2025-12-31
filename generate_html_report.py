#!/usr/bin/env python3
"""
Standalone HTML Report Generator
Generates beautiful HTML report from Allure JSON results WITHOUT needing Allure CLI
"""

import json
import os
from datetime import datetime
from pathlib import Path

def read_allure_results(results_dir='allure-results'):
    """Read all result JSON files from allure-results directory."""
    results = []

    if not os.path.exists(results_dir):
        print(f"Error: {results_dir} directory not found!")
        print("Please run tests first with: behave -f allure_behave.formatter:AllureFormatter -o allure-results")
        return []

    for filename in os.listdir(results_dir):
        if filename.endswith('-result.json'):
            filepath = os.path.join(results_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    results.append(data)
            except Exception as e:
                print(f"Warning: Could not read {filename}: {e}")

    return results

def calculate_metrics(results):
    """Calculate test metrics from results."""
    total = len(results)
    passed = sum(1 for r in results if r.get('status') == 'passed')
    failed = sum(1 for r in results if r.get('status') == 'failed')
    skipped = sum(1 for r in results if r.get('status') == 'skipped')
    broken = sum(1 for r in results if r.get('status') == 'broken')

    total_duration = sum(r.get('stop', 0) - r.get('start', 0) for r in results)
    total_duration_sec = total_duration / 1000 if total_duration else 0

    pass_rate = (passed / total * 100) if total > 0 else 0

    return {
        'total': total,
        'passed': passed,
        'failed': failed,
        'skipped': skipped,
        'broken': broken,
        'pass_rate': pass_rate,
        'duration': total_duration_sec
    }

def format_duration(seconds):
    """Format duration in human-readable format."""
    if seconds < 60:
        return f"{seconds:.1f}s"
    else:
        minutes = int(seconds / 60)
        secs = seconds % 60
        return f"{minutes}m {secs:.1f}s"

def generate_html_report(results, metrics, output_file='test_report.html'):
    """Generate standalone HTML report."""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EM2M Test Automation - Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .header {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        .header h1 {{
            color: #2d3748;
            font-size: 2em;
            margin-bottom: 10px;
        }}

        .header .subtitle {{
            color: #718096;
            font-size: 1.1em;
        }}

        .metrics {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}

        .metric-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
        }}

        .metric-card .value {{
            font-size: 3em;
            font-weight: bold;
            margin: 10px 0;
        }}

        .metric-card .label {{
            color: #718096;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .metric-card.passed .value {{ color: #48bb78; }}
        .metric-card.failed .value {{ color: #f56565; }}
        .metric-card.skipped .value {{ color: #cbd5e0; }}
        .metric-card.total .value {{ color: #4299e1; }}

        .chart-container {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        .progress-bar {{
            width: 100%;
            height: 40px;
            background: #e2e8f0;
            border-radius: 20px;
            overflow: hidden;
            margin: 20px 0;
        }}

        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #48bb78, #38a169);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 1.2em;
            transition: width 1s ease-in-out;
        }}

        .test-list {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        .test-item {{
            padding: 20px;
            border-left: 4px solid #cbd5e0;
            margin-bottom: 15px;
            background: #f7fafc;
            border-radius: 5px;
            transition: transform 0.2s;
        }}

        .test-item:hover {{
            transform: translateX(5px);
        }}

        .test-item.passed {{ border-left-color: #48bb78; }}
        .test-item.failed {{ border-left-color: #f56565; }}
        .test-item.skipped {{ border-left-color: #cbd5e0; }}

        .test-name {{
            font-size: 1.2em;
            font-weight: 600;
            color: #2d3748;
            margin-bottom: 10px;
        }}

        .test-status {{
            display: inline-block;
            padding: 5px 15px;
            border-radius: 15px;
            font-size: 0.85em;
            font-weight: 600;
            text-transform: uppercase;
        }}

        .test-status.passed {{
            background: #c6f6d5;
            color: #22543d;
        }}

        .test-status.failed {{
            background: #fed7d7;
            color: #742a2a;
        }}

        .test-status.skipped {{
            background: #e2e8f0;
            color: #4a5568;
        }}

        .test-duration {{
            color: #718096;
            font-size: 0.9em;
            margin-left: 15px;
        }}

        .test-steps {{
            margin-top: 15px;
            padding-left: 20px;
        }}

        .step {{
            padding: 8px 0;
            color: #4a5568;
            font-size: 0.95em;
        }}

        .step:before {{
            content: "✓ ";
            color: #48bb78;
            font-weight: bold;
            margin-right: 5px;
        }}

        .footer {{
            text-align: center;
            color: white;
            margin-top: 30px;
            padding: 20px;
        }}

        .pie-chart {{
            width: 200px;
            height: 200px;
            margin: 20px auto;
        }}

        @media (max-width: 768px) {{
            .metrics {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>EM2M Test Automation Report</h1>
            <p class="subtitle">Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        </div>

        <div class="metrics">
            <div class="metric-card total">
                <div class="label">Total Tests</div>
                <div class="value">{metrics['total']}</div>
            </div>
            <div class="metric-card passed">
                <div class="label">Passed</div>
                <div class="value">{metrics['passed']}</div>
            </div>
            <div class="metric-card failed">
                <div class="label">Failed</div>
                <div class="value">{metrics['failed']}</div>
            </div>
            <div class="metric-card skipped">
                <div class="label">Skipped</div>
                <div class="value">{metrics['skipped']}</div>
            </div>
        </div>

        <div class="chart-container">
            <h2 style="color: #2d3748; margin-bottom: 20px;">Pass Rate</h2>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {metrics['pass_rate']:.1f}%">
                    {metrics['pass_rate']:.1f}%
                </div>
            </div>
            <p style="text-align: center; color: #718096; margin-top: 10px;">
                Duration: {format_duration(metrics['duration'])}
            </p>
        </div>

        <div class="test-list">
            <h2 style="color: #2d3748; margin-bottom: 25px;">Test Results</h2>
"""

    # Add individual test results
    for result in sorted(results, key=lambda x: x.get('name', '')):
        name = result.get('name', 'Unknown Test')
        status = result.get('status', 'unknown')
        duration = (result.get('stop', 0) - result.get('start', 0)) / 1000

        # Get steps if available
        steps = result.get('steps', [])
        steps_html = ""
        if steps:
            steps_html = '<div class="test-steps">'
            for step in steps[:5]:  # Show first 5 steps
                step_name = step.get('name', 'Step')
                steps_html += f'<div class="step">{step_name}</div>'
            if len(steps) > 5:
                steps_html += f'<div class="step" style="color: #a0aec0;">... and {len(steps) - 5} more steps</div>'
            steps_html += '</div>'

        html += f"""
            <div class="test-item {status}">
                <div class="test-name">{name}</div>
                <span class="test-status {status}">{status}</span>
                <span class="test-duration">{duration:.2f}s</span>
                {steps_html}
            </div>
        """

    html += """
        </div>

        <div class="footer">
            <p>EM2M Test Automation Framework</p>
            <p style="margin-top: 10px; font-size: 0.9em;">
                Powered by Behave + Selenium + Python
            </p>
        </div>
    </div>

    <script>
        // Animate progress bar on load
        window.addEventListener('load', function() {
            const progressBar = document.querySelector('.progress-fill');
            const width = progressBar.style.width;
            progressBar.style.width = '0%';
            setTimeout(() => {
                progressBar.style.width = width;
            }, 100);
        });
    </script>
</body>
</html>
"""

    # Write HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    return output_file

def main():
    print("=" * 70)
    print("  EM2M Test Automation - HTML Report Generator")
    print("=" * 70)
    print()

    # Read results
    print("[Reading] Reading test results from allure-results/...")
    results = read_allure_results()

    if not results:
        print("[ERROR] No test results found!")
        print("\nPlease run tests first:")
        print("  behave -f allure_behave.formatter:AllureFormatter -o allure-results")
        return

    print(f"[OK] Found {len(results)} test results")

    # Calculate metrics
    print("[Processing] Calculating metrics...")
    metrics = calculate_metrics(results)

    # Generate HTML report
    print("[Generating] Generating HTML report...")
    output_file = generate_html_report(results, metrics)

    print()
    print("=" * 70)
    print("[SUCCESS] REPORT GENERATED SUCCESSFULLY!")
    print("=" * 70)
    print()
    print(f"[Report] Report saved to: {output_file}")
    print(f"[Stats] Total Tests: {metrics['total']}")
    print(f"[Stats] Passed: {metrics['passed']}")
    print(f"[Stats] Failed: {metrics['failed']}")
    print(f"[Stats] Skipped: {metrics['skipped']}")
    print(f"[Stats] Pass Rate: {metrics['pass_rate']:.1f}%")
    print(f"[Stats] Duration: {format_duration(metrics['duration'])}")
    print()
    print("[Browser] Open the report in your browser:")
    print(f"   file:///{os.path.abspath(output_file)}")
    print()

    # Try to open in browser
    try:
        import webbrowser
        webbrowser.open('file://' + os.path.abspath(output_file))
        print("[OK] Report opened in browser!")
    except:
        print("[Note] Manually open the file in your browser")

    print()

if __name__ == '__main__':
    main()
