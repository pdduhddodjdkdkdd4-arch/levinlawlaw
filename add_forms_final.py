import os
import html

# 需要修改的页面列表
PAGES_TO_FIX = [
    'investment-fraud-recovery.html',
    'bank-scam-recovery.html',
    'crypto-rug-pull-recvery.html',
    'cryptocurrency-scam-recovery.html',
    'customer-phishing-protection.html',
    'drained-crypto-wallet-recovery.html',
    'general-online-scam-recovery.html',
    'hack-recovery-services.html',
    'identity-theft-restoration.html',
    'phishing-detection-mitigation.html',
    'ransomeware-decryption-and-recover.html',
    'unauthorized-transaction-reversal.html'
]

# 表单 HTML 代码（包含 CSS 样式）
FORM_HTML = '''								<div class="elementor-element elementor-element-d6c697f elementor-widget elementor-widget-wpforms" data-id="d6c697f" data-element_type="widget" data-e-type="widget" data-settings='{"ultimate_floating_fx_translate_y":{"unit":"px","size":"","sizes":[]}}' data-widget_type="wpforms.default">
									<div class="elementor-widget-container">
										<div class="ultimate__form__wrapper contact__form__style__1">
											<style>
												/* 平滑滚动 */
												html {
													scroll-behavior: smooth;
												}

												/* 锚点偏移补偿 */
												#contact-main-form {
													scroll-margin-top: 100px;
													/* 导航栏高度 + 10px 预留空间 */
												}

												.contact-form-container {
													max-width: 600px;
													margin: 0 auto;
												}

												.contact-form-container h2 {
													font-size: 28px;
													font-weight: 600;
													color: #1a1a2e;
													margin-bottom: 8px;
												}

												.contact-form-container .sub-title {
													font-size: 14px;
													color: #666;
													margin-bottom: 30px;
												}

												.contact-form-container h3 {
													font-size: 18px;
													font-weight: 600;
													color: #1a1a2e;
													margin-bottom: 20px;
													margin-top: 30px;
												}

												.contact-form-container .form-group {
													margin-bottom: 20px;
												}

												.contact-form-container .form-group label {
													display: block;
													font-size: 14px;
													font-weight: 500;
													color: #333;
													margin-bottom: 8px;
												}

												.contact-form-container .form-group label span {
													color: #ff0000;
												}

												.contact-form-container .form-group input {
													width: 100%;
													padding: 12px 15px;
													border: 1px solid #ddd;
													border-radius: 4px;
													font-size: 14px;
													transition: border-color 0.3s;
												}

												.contact-form-container .form-group input:focus {
													outline: none;
													border-color: #0045ff;
												}

												.contact-form-container .form-group .hint {
													font-size: 12px;
													color: #888;
													margin-top: 5px;
												}

												.contact-form-container .submit-btn {
													background-color: #1a1a2e;
													color: #fff;
													border: none;
													padding: 12px 30px;
													border-radius: 4px;
													font-size: 16px;
													font-weight: 500;
													cursor: pointer;
													transition: background-color 0.3s;
												}

												.contact-form-container .submit-btn:hover {
													background-color: #2d2d44;
												}

												.contact-form-container .submit-btn:disabled {
													background-color: #9ca3af;
													cursor: not-allowed;
												}

												/* 验证样式 */
												.contact-form-container .input-error {
													border-color: #dc2626 !important;
													background-color: #fef2f2 !important;
												}

												.contact-form-container .input-error:focus {
													border-color: #dc2626 !important;
													box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1) !important;
												}

												.contact-form-container .form-success {
													background-color: #ecfdf5;
													border: 1px solid #10b981;
													border-radius: 8px;
													padding: 16px;
													margin-bottom: 20px;
													color: #065f46;
												}

												.contact-form-container .form-error-alert {
													background-color: #fef2f2;
													border: 1px solid #dc2626;
													border-radius: 8px;
													padding: 16px;
													margin-bottom: 20px;
													color: #991b1b;
												}
											</style>
											<div class="contact-form-container" id="contact-main-form">
												<!-- 表单区域 -->
												<div id="form-section">
													<h2>Free Consultation</h2>
													<p class="sub-title">Write us anytime, we will answer to
														all
														enquiries within 24 hours.</p>

													<h3>Contact Us.</h3>

													<form id="contact-form" onsubmit="handleFormSubmit(event)">
														<div class="form-group">
															<label>Name <span>*</span></label>
															<input type="text" name="name" required>
														</div>

														<div class="form-group">
															<label>Email <span>*</span></label>
															<input type="email" name="email" required>
														</div>

														<div class="form-group">
															<label>Phone Number (WhatsApp number)
																<span>*</span></label>
															<input type="tel" name="phone" required>
															<p class="hint">Your phone number must be
																registered
																on WhatsApp for easy communication.</p>
														</div>

														<div class="form-group">
															<label>The name of the platform involved in the
																scam
																<span>*</span></label>
															<input type="text" name="platform" required>
														</div>

														<div class="form-group">
															<label>Amount of money defrauded
																<span>*</span></label>
															<input type="text" name="amount" required>
														</div>

														<button type="submit" class="submit-btn">Submit</button>
													</form>
												</div>
											</div>
											<script src="js/csv-manager.js"></script>
											<script>
												document.addEventListener('DOMContentLoaded', function() {
													initContactForm();
												});
											</script>
										</div>
									</div>
								</div>
								<div class="elementor-element elementor-element-d4c499d e-flex e-con-boxed e-con e-parent" data-id="d4c499d" data-element_type="container" data-e-type="container">
									<div class="e-con-inner">
										<div class="elementor-element elementor-element-205fe7a elementor-widget-divider--view-line elementor-widget elementor-widget-divider" data-id="205fe7a" data-element_type="widget" data-e-type="widget" data-settings='{"ultimate_floating_fx_translate_y":{"unit":"px","size":"","sizes":[]}}' data-widget_type="divider.default">
											<div class="elementor-widget-container">
												<div class="elementor-divider">
													<span class="elementor-divider-separator">
													</span>
												</div>
											</div>
										</div>
									</div>
								</div>
								'''


def process_page(page_name):
    file_path = os.path.join(r'c:\Users\电脑\Desktop\us.com', page_name)

    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {page_name}")
        return False

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 检查是否已经有表单元素 d6c697f，如果有，先删除旧的
    if 'elementor-element-d6c697f' in content:
        print(f"  INFO: Found existing form in {page_name}, removing it first...")
        # 找到 form 开始的位置
        widget_start = content.find('elementor-element-d6c697f')
        # 找到开始标签的 <div
        actual_start = content.rfind('<div', 0, widget_start)
        # 找到结束的位置 - 找到下一个 elementor-element-8e8f95e（Clients Feedback 容器）
        end_marker = 'elementor-element-8e8f95e'
        end_pos = content.find(end_marker, actual_start)
        if end_pos != -1:
            content = content[:actual_start] + content[end_pos:]
            print(f"  INFO: Removed old form from {page_name}")

    # 现在在 Clients Feedback 之前添加新的表单
    # 找到 elementor-element-8e8f95e（开始 Clients Feedback 的容器）
    feedback_marker = 'elementor-element-8e8f95e'
    feedback_pos = content.find(feedback_marker)

    if feedback_pos == -1:
        print(f"WARNING: Could not find Clients Feedback section in {page_name}")
        return False

    # 找到 feedback 容器的开始 div 之前的空行或者前一个元素的结束位置
    # 我们需要找到前面最近的 </div> 或者空行的位置
    # 从 feedback_pos 往前找，找到最近的完整行结束
    prev_newline = content.rfind('\n', 0, feedback_pos)
    # 再找前一个换行
    prev_prev_newline = content.rfind('\n', 0, prev_newline)
    # 在这两个换行之间插入表单
    insert_pos = prev_prev_newline + 1

    # 检查这个位置的内容是不是空行或者合适的插入位置
    before_content = content[insert_pos:prev_newline]
    if not before_content.strip() or 'elementor-element' in before_content:
        # 这是一个合适的插入位置
        new_content = content[:insert_pos] + FORM_HTML + content[insert_pos:]
    else:
        # 如果不是，就在 prev_newline 之前插入
        new_content = content[:prev_newline] + FORM_HTML + content[prev_newline:]

    # 保存文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"OK: Successfully processed {page_name}")
    return True


def main():
    print("Starting to add forms to all pages...")
    print("=" * 60)

    success_count = 0
    for page in PAGES_TO_FIX:
        print(f"\nProcessing {page}...")
        if process_page(page):
            success_count += 1

    print("\n" + "=" * 60)
    print(f"Done! Successfully processed {success_count}/{len(PAGES_TO_FIX)} pages.")


if __name__ == "__main__":
    main()
