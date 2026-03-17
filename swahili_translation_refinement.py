"""Program to demonstrate Swahili translation refinement examples."""


class TranslationExample:
    """Store one translation refinement example."""

    def __init__(
        self,
        description,
        description_sw,
        description_sw_refined,
        error_comment,
        improvement_comment,
    ):
        self.description = (description)
        self.description_sw = (description_sw)
        self.description_sw_refined = (description_sw_refined)
        self.error_comment = (error_comment)
        self.improvement_comment = (improvement_comment)


def build_examples():
    """Create and return multiple translation refinement examples."""
    examples = [
        # Issue: Subject agreement was wrong ("mchoro inaonyesha").
        # Better: "unaonyesha" matches "mchoro" and "kokotoa" is a more academic verb.
        TranslationExample(
            "The diagram shows a plant cell. Calculate its length.",
            "Mchoro inaonyesha seli ya mmea. Hesabu urefu wake.",
            "Mchoro unaonyesha seli ya mmea. Kokotoa urefu wake.",
            "The verb agreement and technical verb choice were inaccurate.",
            "The corrected sentence uses proper grammar and scientific wording.",
        ),
        # Issue: Machine translation used awkward literal wording for the independent variable.
        # Better: Uses natural academic phrasing and clear research terminology.
        TranslationExample(
            "In this experiment, temperature is the independent variable.",
            "Katika hii jaribio, joto ni tofauti huru.",
            "Katika jaribio hili, halijoto ndiyo kigezo huru.",
            "Noun class and terminology were unnatural.",
            "The refined version uses standard scientific terms used in Swahili education.",
        ),
        # Issue: "bacteria zinakua" is understandable but informal in this context.
        # Better: "hukua" and "haraka zaidi" sound more natural in academic explanation.
        TranslationExample(
            "Bacteria grow faster in warm conditions.",
            "Bakteria zinakua haraka kwa hali ya joto.",
            "Bakteria hukua kwa kasi zaidi katika mazingira ya joto.",
            "The machine output was understandable but stylistically weak.",
            "The correction improves flow and scientific tone.",
        ),
        # Issue: "kiasi cha wastani" is redundant and the phrase was clumsy.
        # Better: "kiasi cha wastani" replaced by precise term "wastani" and smoother syntax.
        TranslationExample(
            "Find the average speed of the moving object.",
            "Tafuta kasi ya kiasi cha wastani ya kitu kinachosonga.",
            "Tafuta wastani wa kasi ya kitu kinachosogea.",
            "There was redundancy and unnatural word order.",
            "The refined sentence is concise and mathematically natural.",
        ),
        # Issue: "eleza nini kutokea" is grammatically broken.
        # Better: Proper verb form and connective phrase clarify causation.
        TranslationExample(
            "Describe what happens when the pressure increases.",
            "Eleza nini kutokea wakati shinikizo inaongezeka.",
            "Eleza kinachotokea shinikizo linapoongezeka.",
            "The sentence had broken grammar and agreement errors.",
            "The correction applies proper tense linkage and noun-class agreement.",
        ),
        # Issue: "Nyingi data" and "imekusanywa" agreement was incorrect.
        # Better: "Data nyingi zimekusanywa" follows standard usage.
        TranslationExample(
            "A lot of data were collected during the field study.",
            "Nyingi data ilikusanywa wakati wa utafiti wa shamba.",
            "Data nyingi zilikusanywa wakati wa utafiti wa uwandani.",
            "Word order and agreement were incorrect.",
            "The refined sentence uses proper structure and academic register.",
        ),
        # Issue: "chora grafu inayoonyesha uhusiano" lacked precise academic flow.
        # Better: "onesha uhusiano" is cleaner and common in classroom science.
        TranslationExample(
            "Draw a graph showing the relationship between mass and volume.",
            "Chora grafu inaonyesha uhusiano kati ya uzito na ujazo.",
            "Chora grafu inayoonesha uhusiano kati ya massa na ujazo.",
            "The machine translation used less precise scientific vocabulary.",
            "The corrected sentence improves term accuracy and fluency.",
        ),
        # Issue: "kufyonzwa" spelling and structure were awkward.
        # Better: "kufyonzwa" corrected to accepted term and sentence made natural.
        TranslationExample(
            "Nutrients are absorbed through the small intestine.",
            "Virutubisho vinafyonzwa kupitia utumbo mdogo.",
            "Virutubisho hufyonzwa kupitia utumbo mwembamba.",
            "The anatomical term was not the most accurate for this context.",
            "The refinement uses preferred biology terminology in Swahili.",
        ),
        # Issue: "matokeo zinaonyesha" had noun-class mismatch.
        # Better: "matokeo yanaonyesha" fixes agreement and improves readability.
        TranslationExample(
            "The results indicate that the hypothesis was correct.",
            "Matokeo zinaonyesha kwamba nadharia ilikuwa sahihi.",
            "Matokeo yanaonyesha kwamba dhana tete ilikuwa sahihi.",
            "There was noun-class disagreement and an imprecise term.",
            "The corrected version uses proper agreement and scientific vocabulary.",
        ),
        # Issue: "ongeza nguvu mpaka chemsha" omitted key particles.
        # Better: Adds proper object marker and imperative flow.
        TranslationExample(
            "Heat the solution until it boils.",
            "Pasha suluhisho mpaka chemka.",
            "Pasha suluhisho hilo hadi lichemke.",
            "The machine translation dropped grammatical markers.",
            "The correction gives a complete and natural lab instruction.",
        ),
        # Issue: Literal translation of "climate change affects biodiversity" was stiff.
        # Better: More natural verb and established environmental terminology.
        TranslationExample(
            "Climate change affects biodiversity in many regions.",
            "Mabadiliko ya tabia nchi inaathiri utofauti wa viumbe katika maeneo mengi.",
            "Mabadiliko ya tabianchi yanaathiri bioanuwai katika maeneo mengi.",
            "The machine output used awkward and inconsistent terminology.",
            "The refined form uses accepted environmental science terms.",
        ),
        # Issue: "kikomo cha mmenyuko" was unclear in chemistry instruction.
        # Better: "kiwango cha mmenyuko" is the standard phrase.
        TranslationExample(
            "Catalysts increase the rate of reaction without being consumed.",
            "Vichocheo huongeza kikomo cha mmenyuko bila kutumika.",
            "Vichocheo huongeza kiwango cha mmenyuko bila yenyewe kutumika.",
            "The key chemistry term was mistranslated.",
            "The corrected sentence preserves scientific meaning accurately.",
        ),
    ]
    return examples


def print_comparisons(examples):
    """Print English text, machine translation, and refined translation."""
    for index, example in enumerate(examples, start=1):
        print(f"Example {index}")
        print(f"English: {example.description}")
        print(f"Machine Swahili: {example.description_sw}")
        print(f"Refined Swahili: {example.description_sw_refined}")
        print(f"Issue: {example.error_comment}")
        print(f"Why better: {example.improvement_comment}")
        print("-" * 72)


if __name__ == "__main__":
    translation_examples = build_examples()
    print_comparisons(translation_examples)
