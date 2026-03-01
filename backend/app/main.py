from app.retrieval.retriever import Retriever
from app.generation.generator import Generator
from app.evaluation.metrics import precision_at_k
from app.evaluation.noise import noise_ratio
from app.evaluation.benchmark import measure_time


if __name__=="__main__":

    retriever=Retriever()
    generator=Generator()

    query="When does model replacement improve consumer welfare?"

    # --- Retrieve + Measure Retrieval Time ---
    results,retrieval_time = measure_time(
        retriever.retrieve,
        query,
        3
    )

    relevant_keywords = [
        "model replacement",
        "monotonicity",
        "non-monotone",
        "BTL aggregation",
        "consumer welfare",
        "monotone region",
        "noise level",
        "beta",
    ]
    # ================= FIXED =================
    fixed_top=results["fixed"][0]
    fixed_precision=precision_at_k(results["fixed"],relevant_keywords)
    fixed_noise=noise_ratio(results["fixed"],relevant_keywords)

    fixed_answer=generator.generate(query,results["fixed"])

    print("\n================ FIXED =================")
    print("Top Score:",round(fixed_top["score"],4))
    print("Precision@3:",round(fixed_precision,4))
    print("Noise Ratio:",round(fixed_noise,4))
    print("Retrieval Time:",round(retrieval_time,4),"seconds")
    print("\nGenerated Answer:\n")
    print(fixed_answer)


    # ================= SEMANTIC =================
    semantic_top=results["semantic"][0]
    semantic_precision=precision_at_k(results["semantic"],relevant_keywords)
    semantic_noise=noise_ratio(results["semantic"],relevant_keywords)

    semantic_answer=generator.generate(query,results["semantic"])

    print("\n================ SEMANTIC =================")
    print("Top Score:",round(semantic_top["score"],4))
    print("Precision@3:",round(semantic_precision,4))
    print("Noise Ratio:",round(semantic_noise,4))
    print("Retrieval Time:",round(retrieval_time,4),"seconds")
    print("\nGenerated Answer:\n")
    print(semantic_answer)

    retriever.close()