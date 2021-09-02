# Locat-Tentes
<t t-if="line.price_with_installation == 0">
                <t t-set="current_subtotal_with_installation" t-value="current_subtotal_with_installation + line.price_unit"/>    
            </t>

            <t t-if="line.price_with_installation &gt; 0">
                <t t-set="current_subtotal_with_installation" t-value="current_subtotal_with_installation + line.price_with_installation"/>
            </t>